import re
import PyPDF2

# Extract text from PDF
def extract_text(file):
    text = ""
    try:
        pdf = PyPDF2.PdfReader(file)
        for page in pdf.pages:
            text += page.extract_text() or ""
    except:
        return ""
    return text

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    return text

# Extract skills
def extract_skills(text, skills_db):
    found_skills = []
    for skill in skills_db:
        if skill.lower() in text:
            found_skills.append(skill)
    return list(set(found_skills))
