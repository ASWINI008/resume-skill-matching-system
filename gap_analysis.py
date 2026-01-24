def find_skill_gap(resume_skills, jd_skills):
    """
    Identify missing skills based on job requirements.
    """

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    missing_skills = list(jd_set - resume_set)

    return missing_skills
