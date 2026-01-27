import re

def clean_job_description(text):
    """
    Cleans and normalizes job description text.
    """

    # convert to lowercase
    text = text.lower()

    # remove special characters
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()
