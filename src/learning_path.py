def generate_learning_path(missing_skills):
    """
    Generates a simple, motivating, and beginner-friendly learning path.
    Strictly 3 steps per skill. Short and catchy.
    """
    roadmap = {}
    
    # Strictly 3 short, motivating steps per skill
    custom_steps = {
        "python": [
            "Learn Python basics like variables and loops.",
            "Solve 5 simple logic puzzles online.",
            "Write a script to automate a small task."
        ],
        "sql": [
            "Master SELECT queries to fetch data.",
            "Learn to JOIN tables like a pro.",
            "Build a simple database for your hobby."
        ],
        "java": [
            "Understand variables and classes closely.",
            "Check how Objects interact in memory.",
            "Code a basic calculator app."
        ],
        "javascript": [
            "Change HTML content using JS code.",
            "Add click events to simple buttons.",
            "Build a 'To-Do List' website."
        ],
        "machine learning": [
            "Learn what ML is with simple videos.",
            "Try a linear regression tutorial.",
            "Predict house prices with a dataset."
        ],
        "react": [
            "Learn Components and Props concepts.",
            "Manage state with useState hook.",
            "Build a small weather widget."
        ],
        "html": [
            "Learn standard tags like div and p.",
            "Structure a simple 'About Me' page.",
            "Add links and images to your site."
        ],
        "css": [
            "Learn colors, fonts, and box model.",
            "Style a simple button to look cool.",
            "Create a responsive card layout."
        ],
        "flask": [
            "Make a 'Hello World' Flask route.",
            "Render HTML templates with Jinja.",
            "Connect a form to your backend."
        ],
        "django": [
            "Start a project and create an app.",
            "Define Models for your database.",
            "Build a simple blog post view."
        ]
    }
    
    for skill in missing_skills:
        s_lower = skill.lower()
        
        if s_lower in custom_steps:
            roadmap[skill] = custom_steps[s_lower]
        else:
            # Fallback must also be exactly 3 steps, short & motivating
            roadmap[skill] = [
                f"Watch a 5-minute intro video on {skill.title()}.",
                f"Follow a 'Hello World' tutorial for {skill.title()}.",
                f"Build a tiny demo to test your skills."
            ]
            
    return roadmap
