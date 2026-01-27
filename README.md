# SkillSync Pro  
### AI-Powered Resume Screening & Skill Matching System

SkillSync Pro is an intelligent resume analysis and career guidance platform designed for **students, recruiters, and training institutions**.  
It automates resume screening, skill matching, learning gap detection, learning path generation, and candidate ranking using NLP-based techniques.

---

## Project Overview

Manual resume screening is time-consuming and inconsistent. SkillSync Pro solves this by providing an AI-assisted system that:

- Analyzes resumes automatically  
- Matches skills with job descriptions  
- Identifies missing skills  
- Generates personalized learning paths  
- Recommends suitable job roles  
- Ranks candidates for recruiters  

This project includes **separate dashboards for Students and Recruiters**.

---

## Application Screenshots
---

### 🔐 Login Page

<img width="1357" height="562" alt="Screenshot 2026-01-27 134721" src="https://github.com/user-attachments/assets/885a20ba-1d79-49ee-bfc3-60939ee8e1df" />

---

### 📝 Sign Up Page

<img width="1318" height="561" alt="Screenshot 2026-01-27 134734" src="https://github.com/user-attachments/assets/395f58e2-3b81-4b5c-9c5b-25e7fa599356" />

---

### 🎓 Student Dashboard

<img width="1361" height="544" alt="Screenshot 2026-01-27 134818" src="https://github.com/user-attachments/assets/86b727bd-e926-4726-880d-ad2f207f26b6" />

---

### 📤 Resume Upload & Job Description

<img width="1296" height="534" alt="Screenshot 2026-01-27 134857" src="https://github.com/user-attachments/assets/407dd39e-5c7a-45c4-b632-ae112a6462f1" />

---

### 📊 Analysis Insights and ✅ Matched Skills & ❌ Skills to Acquire

<img width="1353" height="553" alt="Screenshot 2026-01-27 134946" src="https://github.com/user-attachments/assets/52645bfb-51de-41bf-b9a9-f302a8d03eb2" />

---

### 💡 Mentor Message & Motivation

<img width="1343" height="555" alt="Screenshot 2026-01-27 135011" src="https://github.com/user-attachments/assets/1561128a-92d1-4928-8a16-e9d4d8869dd8" />

---

### 🧭 Personalized Learning Roadmap

<img width="1255" height="521" alt="Screenshot 2026-01-27 143424" src="https://github.com/user-attachments/assets/67cb89eb-fbec-4520-8ad6-eaa401f42e48" />

---

### 💼 Recommended Career Roles

<img width="1343" height="513" alt="Screenshot 2026-01-27 135028" src="https://github.com/user-attachments/assets/72a2424a-049e-45e6-98b1-c94fd110c2e1" />

---

### 👨‍💼 Recruiter Dashboard

<img width="1342" height="546" alt="Screenshot 2026-01-27 135115" src="https://github.com/user-attachments/assets/d3720355-424b-4dc4-b584-45da0cac1722" />

---

### 📈 Candidate Ranking Table and  Top Performer Identification

<img width="1342" height="557" alt="Screenshot 2026-01-27 135537" src="https://github.com/user-attachments/assets/fabb0efa-1a18-4bb6-b231-511342a50b70" />

---

## 🎯 Project Objectives

- Automate resume screening
- Reduce manual HR effort
- Help students understand skill gaps
- Provide structured learning guidance
- Enable recruiter-side bulk resume comparison

---

## Key Features

### Student Module
- Resume upload (PDF)
- Job description input
- Skill match percentage
- Content match score
- Overall ATS score
- Matched skills list
- Skills to acquire list
- AI mentor motivation message
- Personalized learning roadmap
- Career role recommendations
- Career strategic roadmap explanation

---

### Recruiter Module
- Job description input
- Upload multiple resumes (up to 20)
- Automatic resume comparison
- Candidate ranking
- Skill match percentage comparison
- Missing skill count
- Top performer identification

---

## 📊 Evaluation Metrics

| Metric | Description |
|------|-------------|
| Skill Match % | Skill overlap between resume and JD |
| Content Match % | Semantic similarity |
| Overall Score | Weighted ATS score |
| Missing Skills | Skill gap detection |
| Role Match | Career suitability |

---

## System Architecture

User
│
▼
Streamlit UI (app.py)
│
▼
Flask API (api.py)
│
▼
NLP Processing Modules
│
▼
Analysis & Recommendations


---

## Technologies Used

- Python
- Streamlit
- Flask
- REST API
- NLP
- PDF Text Extraction
- Skill Matching Algorithms

---

## 🔄 Workflow

1. Upload resume and job description  
2. Extract text and preprocess data  
3. Identify skills from resume and JD  
4. Calculate skill & content match  
5. Detect missing skills  
6. Generate learning path  
7. Recommend suitable roles  
8. Rank candidates (recruiter side)

---

## Target Users

- Students  
- College placement cells  
- Training departments  
- Fresher hiring simulations  

---

## Limitations

- Keyword-based NLP approach  
- Best suited for technical resumes  
- No database authentication (demo purpose)  
- Resume format variations may affect results  
- Not intended for enterprise deployment  

---

## 🔮 Future Enhancements

- Database integration  
- Resume improvement suggestions  
- Cloud deployment  
- Advanced AI model integration  
- Admin dashboard  
- Skill proficiency scoring  
- Analytics visualization  

---

## ▶️ How to Run

### Step 1 — Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt

```
### Step 3 — Run backend API
```bash

python api.py

```
### Step 4 — Run frontend
```bash
streamlit run app.py
```
---
🏁 Project Outcome

SkillSync Pro demonstrates how AI-assisted resume screening can:

Improve hiring efficiency

Support student career development

Provide structured learning direction

Reduce recruiter screening effort

