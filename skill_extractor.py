def extract_skills(text):
    """
    Extract skills from text using predefined skill mapping.
    """

    skill_mapping = {
        # Languages
        "python": ["python"],
        "java": ["java"],
        "c++": ["c++", "cpp"],
        "c#": ["c#", "csharp"],
        "go": ["go", "golang"],
        "ruby": ["ruby"],
        "php": ["php"],
        "javascript": ["javascript", "js"],
        "typescript": ["typescript", "ts"],
        "swift": ["swift"],
        "kotlin": ["kotlin"],
        "rust": ["rust"],
        
        # Web & Frameworks
        "html": ["html", "hypertext markup language"],
        "css": ["css", "cascading style sheets"],
        "react": ["react", "reactjs"],
        "angular": ["angular", "angularjs"],
        "vue": ["vue", "vuejs"],
        "node.js": ["node.js", "nodejs", "node"],
        "flask": ["flask"],
        "django": ["django"],
        "spring": ["spring", "springboot"],
        
        # Data & AI
        "sql": ["sql", "mysql", "postgresql", "postgres"],
        "machine learning": ["machine learning", "ml"],
        "deep learning": ["deep learning", "dl"],
        "tensorflow": ["tensorflow", "tf"],
        "pytorch": ["pytorch"],
        "pandas": ["pandas"],
        "numpy": ["numpy"],
        "scikit-learn": ["scikit-learn", "sklearn"],
        "hadoop": ["hadoop"],
        "spark": ["spark"],
        
        # Cloud & DevOps
        "aws": ["aws", "amazon web services"],
        "azure": ["azure"],
        "gcp": ["gcp", "google cloud"],
        "docker": ["docker"],
        "kubernetes": ["kubernetes", "k8s"],
        "terraform": ["terraform"],
        "jenkins": ["jenkins"],
        "git": ["git"]
    }

    found_skills = set()
    text = text.lower()

    for skill, variations in skill_mapping.items():
        for word in variations:
            if word in text:
                found_skills.add(skill)

    return list(found_skills)
