import streamlit as st
from sentence_transformers import SentenceTransformer, util
from utils import extract_text, clean_text, extract_skills

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load skills DB
with open("skills_db.txt") as f:
    skills_db = f.read().splitlines()

st.title("🔥 AI Resume Screening System (Hybrid)")

job_description = st.text_area("Enter Job Description")

uploaded_file = st.file_uploader("Upload Resume", type="pdf")

if uploaded_file and job_description:

    # Extract text
    resume_text = extract_text(uploaded_file)

    # Clean text
    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    # Extract skills
    resume_skills = extract_skills(resume_text, skills_db)
    job_skills = extract_skills(job_description, skills_db)

    # Skill match score
    common = set(resume_skills) & set(job_skills)
    skill_score = len(common) / max(len(job_skills), 1) * 100

    # BERT similarity (skills based)
    resume_embedding = model.encode(" ".join(resume_skills))
    job_embedding = model.encode(" ".join(job_skills))

    score = util.cos_sim(resume_embedding, job_embedding)
    bert_score = score.item() * 100

    # Final score (Hybrid)
    final_score = (skill_score * 0.7) + (bert_score * 0.3)

    # Output
    st.success(f"🎯 Match Score: {final_score:.2f}%")

    if final_score > 70:
        st.success("✅ Strong Match")
    elif final_score > 50:
        st.warning("⚠️ Moderate Match")
    else:
        st.error("❌ Weak Match")

    st.write("### 🧠 Detected Resume Skills:")
    st.write(", ".join(resume_skills))

    st.write("### 📌 Job Required Skills:")
    st.write(", ".join(job_skills))