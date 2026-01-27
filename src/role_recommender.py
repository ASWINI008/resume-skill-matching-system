def recommend_roles(resume_skills):
    """
    Suggests 3-5 suitable entry-level/fresher job roles based on skills.
    Returns a list of dictionaries: [{"role": "Role Name", "reason": "Short reason"}]
    """
    
    # Map skills to Role + Reason Template
    skill_role_map = {
        # Python
        "python": [
            {"role": "Python Junior Developer", "reason": "Matches your Python key skill."},
            {"role": "Django Developer", "reason": "Relevant for web backend roles using Python."},
            {"role": "Backend Trainee", "reason": "Good fit for server-side logic."}
        ],
        "flask": [
             {"role": "API Developer", "reason": "Matches your Flask/REST API knowledge."}
        ],
        
        # Java
        "java": [
            {"role": "Java Associate Developer", "reason": "Matches your core Java skills."},
            {"role": "Software Engineer Trainee", "reason": "Standard entry role for Java profiles."}
        ],
        
        # Web
        "javascript": [
            {"role": "Frontend Developer", "reason": "Matches your JavaScript proficiency."}
        ],
        "react": [
            {"role": "React.js Developer", "reason": "High demand for your React skills."}
        ],
        "html": [
            {"role": "Junior Web Developer", "reason": "Matches your web structure knowledge."}
        ],
        "css": [
            {"role": "UI Trainee", "reason": "Fits your styling and design skills."}
        ],
        
        # Data
        "sql": [
            {"role": "Junior Data Analyst", "reason": "Matches your SQL/Database skills."}
        ],
        "machine learning": [
            {"role": "Junior ML Engineer", "reason": "Matches your Machine Learning background."}
        ]
    }

    suggested_roles = []
    seen_roles = set()
    
    # 1. Direct Skill Matching
    for skill in resume_skills:
        s_lower = skill.lower()
        if s_lower in skill_role_map:
            for item in skill_role_map[s_lower]:
                if item["role"] not in seen_roles:
                    suggested_roles.append(item)
                    seen_roles.add(item["role"])
    
    # 2. General Fallbacks
    if not suggested_roles:
         if "python" in resume_skills or "java" in resume_skills:
             fallback = {"role": "Software Engineer Trainee", "reason": "Fits general coding profile."}
             if fallback["role"] not in seen_roles:
                 suggested_roles.append(fallback)
    
    # 3. Limit to 5
    return suggested_roles[:5]
