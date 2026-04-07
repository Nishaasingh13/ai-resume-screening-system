<<<<<<< HEAD
# ai-resume-screening-system
This project is an AI-based Resume Screening System that automatically analyzes resumes and matches them with job descriptions using Natural Language Processing (NLP) and Machine Learning.  It helps recruiters quickly identify suitable candidates and reduces manual effort.
=======
# 🔥 AI Resume Screening System

## 📌 Overview
This project is an AI-based Resume Screening System that automatically analyzes resumes and matches them with job descriptions using Natural Language Processing (NLP) and Machine Learning.

It helps recruiters quickly identify suitable candidates and reduces manual effort.

---

## 🚀 Features
- 📄 Upload Resume (PDF)
- 🧠 Extract text from resume
- 🔍 Detect skills from resume
- 🎯 Match resume with job description
- 📊 Generate Match Score (%)
- ✅ Strong / Weak match classification

---

## 🛠️ Tech Stack
- Python
- Streamlit (for UI)
- Sentence Transformers (BERT model)
- PyPDF2 (PDF text extraction)
- Regex (text preprocessing)

---

## 🤖 AI Model Used
- SentenceTransformer (`all-MiniLM-L6-v2`)
- Converts text into embeddings
- Calculates similarity using cosine similarity

---

## ⚙️ How It Works

1. User uploads a resume (PDF)
2. System extracts text using PyPDF2
3. Text is cleaned using regex
4. Skills are extracted using a predefined skills database
5. AI model compares resume with job description
6. Hybrid score is calculated:
>>>>>>> c2675a5 (AI Resume Screening System)
