from flask import Flask, request, jsonify
import tempfile
import os
from flask_cors import CORS

from src.resume_loader import extract_resume_text
from src.jd_processor import clean_job_description
from src.skill_extractor import extract_skills
from src.matcher import calculate_match_score
from src.gap_analysis import find_skill_gap
from src.learning_path import generate_learning_path
from src.role_recommender import recommend_roles
from src.mentor import (
    generate_mentor_feedback,
    generate_missing_skills_guidance,
    generate_role_guidance
)

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Resume Skill Matching API is running"

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    try:
        resume_file = request.files.get("resume")
        jd_text = request.form.get("job_description")

        if resume_file is None or jd_text is None:
            return jsonify({"error": "Missing input"}), 400

        # Save resume temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
            resume_path = temp.name
            resume_file.save(resume_path)

        try:
            resume_text = extract_resume_text(resume_path)
        finally:
            if os.path.exists(resume_path):
                os.remove(resume_path)

        jd_cleaned = clean_job_description(jd_text)

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_cleaned)

        # ---------- Skill Match ----------
        skill_match = round(
            (len(set(resume_skills) & set(jd_skills)) / max(len(jd_skills), 1)) * 100, 2
        )

        # ---------- Content Match ----------
        content_match = int(calculate_match_score(resume_text, jd_cleaned))

        # ---------- Overall ----------
        overall_match = round(
            (skill_match * 0.6) + (content_match * 0.4), 2
        )

        # ---------- Gap ----------
        missing_skills = find_skill_gap(resume_skills, jd_skills)

        # ---------- Learning Path ----------
        learning_path = generate_learning_path(missing_skills)

        # ---------- Role Recommendation ----------
        recommended_roles = recommend_roles(resume_skills)

        # ---------- AI Motivation ----------
        mentor_feedback = generate_mentor_feedback(
            resume_skills,
            missing_skills,
            overall_match
        )

        missing_skills_guidance = generate_missing_skills_guidance(missing_skills)

        role_guidance = generate_role_guidance(
            recommended_roles,
            has_missing_skills=bool(missing_skills)
        )

        return jsonify({
            "skill_match": skill_match,
            "content_match": content_match,
            "overall_match": overall_match,
            "resume_skills": resume_skills,
            "missing_skills": missing_skills,
            "learning_path": learning_path,
            "recommended_roles": recommended_roles,
            "mentor_feedback": mentor_feedback,
            "missing_skills_guidance": missing_skills_guidance,
            "role_guidance": role_guidance
        })

    except Exception as e:
        import traceback
        print("CRITICAL ERROR:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)

