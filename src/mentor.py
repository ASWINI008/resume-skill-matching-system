import random

def generate_mentor_feedback(resume_skills, missing_skills, match_score):
    """
    Generates a supportive, professional career mentor message.
    Guidelines: 3-4 lines max, positive, normalizes gaps, no emojis, professional English.
    """
    
    # 1. Base Openers
    if match_score >= 80:
        opener = "You have built a very strong foundation and your profile shows great alignment with the requirements."
    else:
        opener = "It is great to see the initiative you are taking to align your skills with this role."
        
    # 2. Addressing Gaps & Mindset
    if missing_skills:
        gap_context = f"While there are some skills like {', '.join(missing_skills[:2])} to develop, please remember that skill gaps are a normal part of every professional journey."
        encouragement = "Focusing on these areas with a learning mindset will steadily strengthen your expertise for your target path."
    else:
        gap_context = "You have demonstrated all the core competencies requested for this role."
        encouragement = "Your preparation is excellent, and you should feel confident in the specialized skills you have acquired."

    # 3. Closing
    closing = "Keep moving forward with confidence and maintain your commitment to consistent growth."
    
    return f"{opener} {gap_context} {encouragement} {closing}"


def generate_missing_skills_guidance(missing_skills):
    """
    CASE 1: Generates encouraging 2-3 line guidance when missing skills are detected.
    Focuses on growth mindset, normalizing skill gaps, and avoiding demotivation.
    """
    if not missing_skills:
        return None
    
    # Growth mindset messages - 2-3 lines each
    messages = [
        "Every expert was once a beginner. Missing skills are not weaknesses — they're directions for growth. Each skill you learn brings you closer to your dream role.",
        
        "Skill gaps are completely normal, even for experienced professionals. What matters most is your willingness to learn and adapt. You're already on the right path by identifying what to focus on next.",
        
        "The best developers didn't start with all the skills — they built them over time. Your current skill set is your foundation, and these missing skills are simply your next learning adventure.",
        
        "Don't let missing skills discourage you. They're not barriers, they're stepping stones. Every skill you see here is learnable, and many professionals picked them up on the job.",
        
        "Your journey is unique, and comparing yourself to a job description is just one data point. Focus on consistent growth rather than perfect matches. Progress, not perfection, is what counts.",
        
        "Missing a few skills doesn't define your potential — it defines your learning roadmap. Embrace the challenge, and remember that every expert you admire once stood exactly where you are now.",
    ]
    
    return random.choice(messages)


def generate_role_guidance(recommended_roles, has_missing_skills=False):
    """
    CASE 2: Generates gentle explanation for recommended job roles.
    Emphasizes alternative paths, not rejection, and highlights skill evolution.
    """
    if not recommended_roles:
        return "Keep building your skills! As your expertise grows, more role opportunities will align with your profile."
    
    # Supportive messages about alternative career paths
    if has_missing_skills:
        # When there are missing skills, emphasize achievability
        messages = [
            "These roles are suggested based on your current strengths. With a few additional skills, your desired role is absolutely achievable. Think of these as stepping stones, not limitations.",
            
            "Your dream role is within reach! These recommendations show what you can pursue right now while you're building the skills for your target position. Every career path has multiple entry points.",
            
            "These roles match your current skill set and can be excellent starting points. As you gain experience and learn new skills, transitioning to your ideal role becomes much easier. Growth is a journey, not a race.",
            
            "Consider these roles as strategic career moves. They align with what you know today and can provide valuable experience while you develop the skills for your ultimate goal. Many successful professionals took similar paths.",
        ]
    else:
        # When no missing skills, emphasize options and flexibility
        messages = [
            "These roles are great matches for your skill set! You have the flexibility to choose based on your interests and career goals. Your skills open multiple doors.",
            
            "Your diverse skill set qualifies you for various roles. These suggestions highlight different career paths you can explore. Choose the one that excites you most!",
            
            "With your current skills, you have options! These roles represent different ways to apply your expertise. Consider which aligns best with your long-term vision.",
            
            "You're in a strong position with multiple role possibilities. These recommendations show the breadth of opportunities available to you. Trust your instincts on which path feels right.",
        ]
    
    return random.choice(messages)