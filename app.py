import streamlit as st
from sentence_transformers import SentenceTransformer, util
from utils import extract_text, clean_text, extract_skills

# =========================
# LOAD MODEL (FAST)
# =========================
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# Load skills
with open("skills_db.txt") as f:
    skills_db = f.read().splitlines()

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="AI Resume Screener", layout="wide")

# Sidebar Navigation
page = st.sidebar.selectbox("📌 Navigation", ["Home", "Screening", "About"])

# =========================
# HOME PAGE
# =========================
if page == "Home":
    st.markdown("<h1 style='text-align:center;color:#4CAF50;'>🔥 AI Resume Screening System</h1>", unsafe_allow_html=True)
    st.write("### 🚀 Smart AI system to screen and rank resumes")
    st.write("✔ Upload multiple resumes")
    st.write("✔ Get match score & ranking")
    st.write("✔ Identify missing skills")

# =========================
# SCREENING PAGE
# =========================
elif page == "Screening":

    st.title("📄 Resume Screening")

    col1, col2 = st.columns(2)

    with col1:
        job_description = st.text_area("📌 Enter Job Description")

    with col2:
        uploaded_files = st.file_uploader(
            "📄 Upload Multiple Resumes",
            type="pdf",
            accept_multiple_files=True
        )

    if uploaded_files and job_description:

        with st.spinner("Analyzing resumes... 🔍"):

            results = []

            job_clean = clean_text(job_description)
            job_skills = extract_skills(job_clean, skills_db)

            # fallback if no skills
            if not job_skills:
                job_skills = job_clean.split()[:10]

            job_embedding = model.encode(job_clean)

            st.subheader("🧠 Required Skills")
            st.write(", ".join(job_skills))

            for file in uploaded_files:

                resume_text = extract_text(file)

                if not resume_text:
                    st.warning(f"{file.name} has no readable content")
                    continue

                resume_clean = clean_text(resume_text)
                resume_skills = extract_skills(resume_clean, skills_db)

                # Skill score
                skill_score = len(set(resume_skills) & set(job_skills)) / max(len(job_skills), 1)

                # Semantic score
                resume_embedding = model.encode(resume_clean)
                semantic_score = util.cos_sim(job_embedding, resume_embedding).item()

                # Final score
                final_score = (skill_score * 0.6 + semantic_score * 0.4) * 100

                matched = list(set(resume_skills) & set(job_skills))
                missing = list(set(job_skills) - set(resume_skills))

                results.append({
                    "name": file.name,
                    "score": final_score,
                    "matched": matched,
                    "missing": missing
                })

        # Sort results
        results = sorted(results, key=lambda x: x["score"], reverse=True)

        st.subheader("🏆 Candidate Ranking")

        medals = ["🥇", "🥈", "🥉"]

        shortlisted = []

        for i, res in enumerate(results):

            medal = medals[i] if i < 3 else f"#{i+1}"

            # Card UI
            st.markdown(f"""
            <div style="background:white;padding:15px;border-radius:10px;box-shadow:2px 2px 10px #ccc;margin-bottom:10px">
            <h3>{medal} {res['name']}</h3>
            <b>Score:</b> {res['score']:.2f}%
            </div>
            """, unsafe_allow_html=True)

            st.progress(min(int(res["score"]), 100))

            # Best candidate
            if i == 0:
                st.success("🏆 Best Candidate")

            # Match level
            if res["score"] > 75:
                st.success("Strong Match ✅")
            elif res["score"] > 50:
                st.warning("Moderate Match ⚠️")
            else:
                st.error("Weak Match ❌")

            # Skills
            st.write("✔ Matched Skills:", ", ".join(res["matched"]) or "None")
            st.write("❌ Missing Skills:", ", ".join(res["missing"]) or "None")

            # Explanation
            st.info(f"{len(res['matched'])} skills matched out of {len(job_skills)} required")

            # Shortlist
            if st.checkbox(f"Shortlist {res['name']}", key=res['name']):
                shortlisted.append(res['name'])

            st.write("---")

        # Show shortlisted
        if shortlisted:
            st.subheader("📋 Shortlisted Candidates")
            for name in shortlisted:
                st.write(f"✅ {name}")

# =========================
# ABOUT PAGE
# =========================
elif page == "About":

    st.title("ℹ️ About Project")

    
    st.write("""
    This AI Resume Screening System uses NLP and Machine Learning to:
    
    ✔ Analyze resumes  
    ✔ Extract skills  
    ✔ Match with job description  
    ✔ Rank candidates  
    
    Built using:
    - Python
    - Streamlit
    - Sentence Transformers
    """)
