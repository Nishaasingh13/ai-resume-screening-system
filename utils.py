import PyPDF2
import re

# Extract text from PDF
def extract_text(file):
    text = ""
    reader = PyPDF2.PdfReader(file)

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text.lower()


# Clean text
def clean_text(text):
    text = re.sub(r'\W', ' ', text)
    text = text.lower()
    return text


# Extract skills
def extract_skills(text, skills_db):
    found_skills = []

    for skill in skills_db:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))