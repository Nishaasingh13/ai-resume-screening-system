🔥 AI Resume Screening System

📌 Overview

This project is an AI-based Resume Screening System that helps automate the recruitment process by analyzing and ranking resumes based on a given job description.

The system uses Natural Language Processing (NLP) and Machine Learning techniques to evaluate candidate resumes and identify the best match.

---

🚀 Features

- 📄 Upload multiple resumes (PDF)
- 🧠 Automatic skill extraction
- 🎯 Match score calculation
- 🏆 Candidate ranking system
- ✔ Matched skills detection
- ❌ Missing skills identification
- 📊 Score explanation (transparent results)
- 📋 Resume shortlisting option
- ⚡ Fast processing using model caching
- 🎨 Clean and professional UI

---

🧠 How It Works

1. User enters a Job Description
2. Uploads multiple resumes
3. System:
   - Extracts text from resumes
   - Cleans and processes text
   - Identifies skills
   - Compares resumes with job description
   - Calculates match score using:
     - Skill Matching (60%)
     - Semantic Similarity (40%)
4. Displays ranked candidates with scores

---

🛠️ Technologies Used

- Python 🐍
- Streamlit 🎨 (UI)
- Sentence Transformers 🤖 (NLP Model)
- PyPDF2 📄 (PDF Text Extraction)
- Pandas 📊

---

📁 Project Structure

AI Resume Screening System/
│
├── app.py              # Main Streamlit application
├── utils.py            # Helper functions (text extraction, cleaning, skills)
├── skills_db.txt       # Skills database
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

---

▶️ How to Run

1. Clone the repository:

git clone https://github.com/Nishaasingh13/ai-resume-screening-system
cd ai-resume-screening-system

2. Create virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies:

pip install -r requirements.txt

4. Run the application:

streamlit run app.py

---

🎯 Use Case

- HR recruitment automation
- Resume filtering
- Candidate ranking
- Skill gap analysis

---

🔥 Future Improvements

- 📄 PDF report generation
- 🌐 Deployment on cloud
- 🤖 Job role prediction
- 📊 Data visualization dashboard
- 🔐 Login system

---

🎤 Key Highlights

- Combines rule-based + AI-based scoring
- Provides explainable results
- Supports multiple resume comparison
- Designed as a real-world recruitment solution

---

👩‍💻 Author

Nisha Singh
GitHub: https://github.com/Nishaasingh13

---

⭐ If you like this project, give it a star!
