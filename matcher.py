from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_match_score(resume_text, jd_text):
    """
    Calculates semantic similarity between resume and job description
    using sentence embeddings.
    """

    resume_embedding = model.encode([resume_text])
    jd_embedding = model.encode([jd_text])

    similarity = cosine_similarity(resume_embedding, jd_embedding)

    # convert to percentage
    score = similarity[0][0] * 100

    return round(score, 2)
