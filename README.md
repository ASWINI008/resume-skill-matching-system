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
## 🖥️ Application Screenshots

> 📁 Screenshots are stored inside the `screenshots/` folder.

---

### 🔐 Login Page
<img width="1357" height="562" alt="Screenshot 2026-01-27 134721" src="https://github.com/user-attachments/assets/6f9da723-63da-4020-88e6-df4e4a8ddb6e" />

**Purpose:**  
Allows users to select Student or Recruiter role and access the system.

---

### 📝 Sign Up Page
<img width="1318" height="561" alt="Screenshot 2026-01-27 134734" src="https://github.com/user-attachments/assets/64e0776c-2d33-4f71-956b-79323dbf92d5" />

**Purpose:**  
New users can register with role-based access.

---

### 🎓 Student Dashboard
<img width="1361" height="544" alt="Screenshot 2026-01-27 134818" src="https://github.com/user-attachments/assets/9b75bdd3-e08c-4b77-b5d4-9099ef8a53d8" />

**Purpose:**  
Students analyze resumes and understand career readiness.

---

### 📤 Resume Upload & Job Description
<img width="1296" height="534" alt="Screenshot 2026-01-27 134857" src="https://github.com/user-attachments/assets/4ed9b9bf-7661-4a0f-92ca-48fb8147aff7" />

**Purpose:**  
Simulates real ATS screening process.

---

### 📊 Analysis Insights
<img width="1353" height="553" alt="Screenshot 2026-01-27 134946" src="https://github.com/user-attachments/assets/6bbbc9f2-466a-480a-a902-a1c96f14fb2a" />

Displays:
- Skill Match %
- Content Match %
- Overall ATS Score

---

### 💡 Mentor Message & Motivation
<img width="1343" height="555" alt="Screenshot 2026-01-27 135011" src="https://github.com/user-attachments/assets/b3b30dd0-7261-40cd-bd02-7a6026534cbd" />

Provides encouraging guidance to avoid demotivation.

---

### 🧭 Personalized Learning Roadmap
<img width="1255" height="521" alt="Screenshot 2026-01-27 143424" src="https://github.com/user-attachments/assets/bd875872-df0a-4725-831f-07b2176d69a8" />

Step-by-step learning suggestions for missing skills.

---

### 💼 Recommended Career Roles
<img width="1343" height="513" alt="Screenshot 2026-01-27 135028" src="https://github.com/user-attachments/assets/3b3eabf9-c7ea-49b8-9c69-3dc8979f676f" />

Suggests suitable job roles based on current skills.

---

### 👨‍💼 Recruiter Dashboard
<img width="1342" height="546" alt="Screenshot 2026-01-27 135115" src="https://github.com/user-attachments/assets/0b8618bf-509b-4d2c-ac0a-13ca99b0ae1f" />

Allows recruiters to upload multiple resumes.

---

### 📈 Candidate Ranking
<img width="1342" height="557" alt="Screenshot 2026-01-27 135537" src="https://github.com/user-attachments/assets/9d3a7fdc-7cef-4eeb-b176-6453b4cdc989" />

Ranks candidates using ATS score.

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
## System Architecture

```text
+-----------------------------+
|        User Interface       |
|     (Student / Recruiter)   |
+--------------+--------------+
               |
               v
+-----------------------------+
|     Streamlit Frontend      |
|  - Resume Upload (PDF)      |
|  - Job Description Input   |
|  - Dashboard View           |
+--------------+--------------+
               |
               v
+-----------------------------+
|        Flask Backend API    |
|  - /analyze endpoint        |
|  - Request handling         |
+--------------+--------------+
               |
               v
+-----------------------------+
|       Processing Layer      |
|  - Resume Text Extraction   |
|  - JD Cleaning              |
|  - Skill Extraction         |
+--------------+--------------+
               |
               v
+-----------------------------+
|        Analysis Engine      |
|  - Skill Match              |
|  - Content Match            |
|  - ATS Score                |
+--------------+--------------+
               |
               v
+-----------------------------+
|     Recommendation Layer    |
|  - Learning Path            |
|  - Role Recommendation      |
|  - Mentor Guidance          |
+--------------+--------------+
               |
               v
+-----------------------------+
|        Result Display       |
|  - Metrics Visualization    |
|  - Skill Cards              |
|  - Roadmap View             |
+-----------------------------+
```
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
## Folder Structure

```text

resume-skill-matching-system/
│
├── app.py                     # Streamlit frontend
├── api.py                     # Flask backend API
├── requirements.txt
├── README.md
│
├── src/
│   ├── resume_loader.py       # PDF text extraction
│   ├── jd_processor.py        # Job description cleaning
│   ├── skill_extractor.py     # Skill identification
│   ├── matcher.py             # Semantic similarity
│   ├── gap_analysis.py        # Missing skill detection
│   ├── learning_path.py       # Learning roadmap generator
│   └── role_recommender.py    # Job role recommendation
│
├── screenshots/               # Application screenshots
│
└── venv/                      # Virtual environment

```

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

### Live Demo

👉 Application URL:
https://resume-screening-matching.streamlit.app/

Deployed using Streamlit Cloud.

---

🏁 Project Outcome

SkillSync Pro demonstrates how AI-assisted resume screening can:

Improve hiring efficiency

Support student career development

Provide structured learning direction

Reduce recruiter screening effort

