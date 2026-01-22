import pdfplumber

def extract_resume_text(pdf_path):
    """
    Extract text from a resume PDF file.
    """

    resume_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text + "\n"

    return resume_text
