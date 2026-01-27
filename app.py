import streamlit as st
import requests
import pandas as pd
import time
from src.database import register_user, authenticate_user

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SkillSync Pro",
    layout="wide"
)

# --- PREMIUM CSS DESIGN SYSTEM ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    :root {
        --primary: #000000;
        --secondary: #f8fafc;
        --bg-main: #ffffff;
        --text-main: #000000;
        --text-muted: #64748b;
        --border: #000000;
    }

    .stApp {
        background-color: var(--bg-main);
        color: var(--text-main);
        font-family: 'Inter', sans-serif;
    }

    /* Primary Button Hover (Opposite Color) */
    div.stButton > button:first-child {
        background-color: #000000;
        color: #ffffff;
        border: 2px solid #000000;
        transition: all 0.3s ease;
    }

    div.stButton > button:first-child:hover {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
    }

    /* Tabs Hover/Active (Opposite Color) */
    button[data-baseweb="tab"] {
        color: #64748b !important;
    }

    button[data-baseweb="tab"]:hover {
        color: #000000 !important;
    }

    button[aria-selected="true"] {
        color: #000000 !important;
        border-bottom-color: #000000 !important;
    }

    /* Visibility Fixes */
    [data-testid="stFileUploaderFileName"], .stMarkdown p, label, .stTable, [data-testid="stDataFrame"], .stTable td, .stTable th {
        color: var(--text-main) !important;
    }

    /* Metric Value Color */
    [data-testid="stMetricValue"] {
        color: #000000 !important;
    }

</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'auth' not in st.session_state:
    st.session_state.auth = {'logged_in': False, 'role': None, 'user': None}
if 'results' not in st.session_state:
    st.session_state.results = None
if 'active_role' not in st.session_state:
    st.session_state.active_role = None

# --- HELPERS ---
def check_backend():
    try: return requests.get("http://127.0.0.1:5000/", timeout=0.5).status_code == 200
    except: return False

def call_api(resume_file, jd_text):
    try:
        files = {"resume": ("resume.pdf", resume_file.getvalue(), "application/pdf")}
        data = {"job_description": jd_text}
        r = requests.post("http://127.0.0.1:5000/analyze", files=files, data=data, timeout=30)
        if r.status_code == 200:
            return r.json(), None
        else:
            return None, f"Server Error ({r.status_code}): {r.text}"
    except requests.exceptions.Timeout:
        return None, "The request timed out. The server might be busy processing the AI models."
    except Exception as e:
        return None, f"Connection Error: {str(e)}"

# --- UI COMPONENTS ---
def render_metrics(res):
    c1, c2, c3 = st.columns(3)
    c1.metric("Skill Match", f"{res.get('skill_match', 0)}%")
    c2.metric("Content Match", f"{res.get('content_match', 0)}%")
    c3.metric("Overall Score", f"{res.get('overall_match', 0)}%")

# --- PAGES ---
def show_auth():
    st.write("") # Spacing
    st.write("") # Spacing
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown("<h1 style='text-align:center;'>SkillSync <span style='color:#000000'>Pro</span></h1>", unsafe_allow_html=True)
        t1, t2 = st.tabs(["Login", "Sign Up"])
        with t1:
            user = st.text_input("Username")
            pwd = st.text_input("Password", type="password")
            if st.button("Sign In", type="primary", use_container_width=True):
                user_data = authenticate_user(user, pwd)
                if user_data:
                    st.session_state.auth = {'logged_in': True, 'role': user_data['role'], 'user': user_data['username']}
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
        with t2:
            new_role = st.selectbox("Join as", ["Student", "Recruiter"], key="s_role")
            new_username = st.text_input("Choose Username", key="s_user")
            new_name = st.text_input("Full Name", placeholder="e.g. John Doe")
            new_email = st.text_input("Email Address")
            new_pwd = st.text_input("Create Password", type="password", key="s_pass")
            if st.button("Create Account", type="primary", use_container_width=True):
                if new_username and new_name and new_email and new_pwd:
                    success, msg = register_user(new_username, new_name, new_email, new_pwd, new_role)
                    if success:
                        st.success(msg)
                    else:
                        st.error(msg)
                else:
                    st.error("Please fill in all details.")

def show_student():
    st.markdown(f"### 🎓 Student Analysis | Welcome {st.session_state.auth['user']}")
    if st.button("Log Out"):
        st.session_state.auth = {'logged_in': False, 'role': None, 'user': None}
        st.rerun()
    
    st.divider()
    
    # Input Section
    st.markdown("####  1. Upload & Analyze")
    c1, c2 = st.columns(2)
    with c1:
        res_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
    with c2:
        jd_text = st.text_area("Job Description", height=150)
    
    if st.button("Evaluate Profile", type="primary", use_container_width=True):
        print(f"Evaluate Button Clicked - User: {st.session_state.auth['user']}")
        if res_file and jd_text:
            print(f"Inputs detected - Resume size: {len(res_file.getvalue())} bytes")
            with st.spinner("Analyzing profile with AI models..."):
                results, error = call_api(res_file, jd_text)
                if error:
                    print(f"API Error: {error}")
                    st.error(error)
                    st.session_state.results = None
                else:
                    print(f"API Success - Match Score: {results.get('overall_match')}")
                    st.session_state.results = results
                    st.rerun() # Force refresh to show results
        else:
            print("Warning: Missing inputs")
            st.warning("Please upload a resume and provide a job description.")
    
    # Results Section (Visible on same page)
    if st.session_state.results:
        res = st.session_state.results
        st.divider()
        st.markdown("### 📊 Analysis Insights")
        render_metrics(res)
        
        st.write("") # Spacing
        
        # 1. Skills Comparison Section
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### ✅ Matched Skills")
            with st.container():
                if res.get("resume_skills"):
                    skills_list = "".join([f"<li style='margin-bottom:5px; font-weight:600;'>{s.title()}</li>" for s in res.get("resume_skills", [])])
                    st.markdown(f"""
                        <div style='background-color: #ffffff; color: #000000; padding: 20px; border-radius: 12px; height: 100%; border: 2px solid #000000;'>
                            <p style='color: #000000; opacity: 0.7; margin-bottom: 10px;'>High alignment confirmed in:</p>
                            <ul style='list-style-type: none; padding: 0;'>{skills_list}</ul>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("<div style='background: #f8fafc; padding:20px; border-radius:12px; border: 1px dashed #ccc;'>No matching skills detected.</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("#### Skills to Acquire")
            with st.container():
                if res.get("missing_skills"):
                    missing_list = "".join([f"<li style='margin-bottom:5px; font-weight:600;'>{s.title()}</li>" for s in res.get("missing_skills", [])])
                    st.markdown(f"""
                        <div style='background-color: #ffffff; color: #000000; padding: 20px; border-radius: 12px; height: 100%; border: 2px solid #000000;'>
                            <p style='color: #000000; opacity: 0.7; margin-bottom: 10px;'>Bridge the gap with these areas:</p>
                            <ul style='list-style-type: none; padding: 0;'>{missing_list}</ul>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("<div style='background: #ffffff; padding:20px; border-radius:12px; border: 2px solid #000000;'>Elite Profile: No missing skills found!</div>", unsafe_allow_html=True)

        st.write("") # Spacing
        st.divider()

        # 2. Mentor Message Section
        if res.get('mentor_feedback'):
            st.markdown("#### 💡 Mentor Message")
            st.info(f"*{res.get('mentor_feedback')}*")
            
        if res.get("missing_skills_guidance"):
            with st.expander(" Pro-Tip: How to bridge the gap"):
                st.write(res.get("missing_skills_guidance"))
            
        st.write("") # Spacing
        st.divider()

        # 3. Learning Path Section
        if res.get("learning_path"):
            st.markdown("#### Personalized Learning Roadmaps")
            st.caption("Step-by-step guidance to master your missing skills.")
            for skill, steps in res.get("learning_path").items():
                with st.expander(f"Path to Master {skill.title()}"):
                    for i, step in enumerate(steps): 
                        st.markdown(f"**Phase {i+1}:** {step}")
                    
        st.write("") # Spacing
        st.divider()

        # 4. Suggested Career Paths
        if res.get("recommended_roles"):
            st.markdown("#### Suggested Career Paths Based on Your Skills")
            if res.get("role_guidance"): 
                st.caption(f"_{res.get('role_guidance')}_")
            
            role_cols = st.columns(3)
            roles = res.get("recommended_roles")[:3]
            for i, role in enumerate(roles):
                role_name = role.get('role') if isinstance(role, dict) else role
                with role_cols[i]:
                    st.markdown(f"""
                        <div style='background-color: #000000; color: #ffffff; padding: 15px; border-radius: 8px; text-align: center; margin-bottom: 10px;'>
                            <strong style='font-size: 1.1rem;'>{role_name}</strong>
                        </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"View details for {role_name}", key=f"btn_{i}", use_container_width=True):
                        st.session_state.active_role = role_name

            # Role Details Sub-section
            if st.session_state.active_role:
                st.write("")
                with st.container():
                    st.markdown(f"""
                        <div style='border: 2px solid #000000; padding: 25px; border-radius: 12px; background-color: #f8fafc;'>
                            <h4 style='margin-top:0;'> Career Strategic Roadmap: {st.session_state.active_role}</h4>
                            <p style='font-style: italic; color: #333;'>As a {st.session_state.active_role}, you will leverage your strengths in {', '.join(res.get('resume_skills', [])[:2])} to excel. We recommend prioritizing {', '.join(res.get('missing_skills', [])[:1])} through hands-on projects and industry certifications. This path aligns with your current expertise while offering clear technical growth.</p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.write("")
                    if st.button("Close Roadmap", type="secondary"):
                        st.session_state.active_role = None
                        st.rerun()

def show_recruiter():
    st.markdown(f"###  Recruiter Dashboard | Welcome {st.session_state.auth['user']}")
    if st.button("Log Out"):
        st.session_state.auth = {'logged_in': False, 'role': None, 'user': None}
        st.rerun()
    
    st.divider()
    
    # Single Page Recruiter View
    st.markdown("####  Compare & Rank Candidates")
    jd_input = st.text_area("Job Description", height=100)
    files = st.file_uploader("Upload Resumes", type="pdf", accept_multiple_files=True)
    
    if st.button("Apply Ranking", type="primary", use_container_width=True):
        if files and jd_input:
            ranks = []
            progress = st.progress(0)
            for i, f in enumerate(files):
                result, error = call_api(f, jd_input)
                if result:
                    ranks.append({
                        "Candidate": f.name,
                        "Overall Match (%)": round(result.get("overall_match", 0), 1),
                        "Skill Match (%)": round(result.get("skill_match", 0), 1),
                        "Missing Skills": result.get("missing_skills", [])
                    })
                elif error:
                    st.error(f"Error analyzing {f.name}: {error}")
                progress.progress((i+1)/len(files))
            
            if ranks:
                df = pd.DataFrame(ranks).sort_values("Overall Match (%)", ascending=False)
                st.session_state.recruiter_results = df
    
    if hasattr(st.session_state, 'recruiter_results'):
        st.divider()
        st.markdown("####  Candidate Talent Ranking")
        
        # Format the dataframe for display
        display_df = st.session_state.recruiter_results.copy()
        display_df["Missing Skills"] = display_df["Missing Skills"].apply(len)
        st.dataframe(display_df, use_container_width=True, hide_index=True)
        
        # Highlight the best candidate at the end
        if not display_df.empty:
            best_candidate = display_df.iloc[0]
            st.write("")
            st.markdown(f"""
                <div style='background-color: #f0f9ff; color: #0c4a6e; padding: 30px; border-radius: 12px; border: 2px solid #bae6fd; text-align: center;'>
                    <h2 style='margin: 0; color: #0369a1;'> TOP PERFORMER</h2>
                    <hr style='border: 1px solid #bae6fd;'>
                    <p style='margin: 15px 0; font-size: 1.8rem; font-weight: 800; color: #1e293b;'>{best_candidate['Candidate']}</p>
                    <div style='font-size: 2.5rem; font-weight: 900; background: #0369a1; color: #ffffff; display: inline-block; padding: 5px 20px; border-radius: 8px;'>{best_candidate['Overall Match (%)']}% Match</div>
                    <p style='margin-top: 20px; font-size: 1.1rem; color: #075985; opacity: 0.8;'>Highest quality match identified for this requirement.</p>
                </div>
            """, unsafe_allow_html=True)

# --- STATUS BAR ---
if not check_backend():
    st.error("Backend API Offline. Please ensure 'api.py' is running.")
else:
    st.caption("🟢 Server Online | AI Models Loaded")

# --- APP FLOW ---
if not st.session_state.auth['logged_in']: show_auth()
elif st.session_state.auth['role'] == 'student': show_student()
else: show_recruiter()