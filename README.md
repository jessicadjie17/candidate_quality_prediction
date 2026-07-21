# 🤖 TalentMatch AI
### AI-Assisted Hiring Decision Support System

TalentMatch AI is a machine learning-based decision support system designed to assist recruiters in making more objective, consistent, and explainable hiring decisions after the candidate assessment process.

---

# 🔍 Problem Statement

Recruitment decisions require recruiters to evaluate multiple candidate attributes, including education, work experience, technical assessments, interview performance, soft skills, and referrals. Although structured assessments are available, final hiring decisions may still be influenced by subjective judgment, leading to inconsistent evaluations across candidates.

To address this challenge, TalentMatch AI provides **AI-assisted hiring recommendations** that support recruiters during the final hiring stage. The system is designed to **support—not replace—human decision-making**, enabling recruiters to make more consistent and data-driven hiring decisions.

---

# 🎯 Solution

TalentMatch AI predicts whether a candidate is **Eligible** or **Not Eligible** based on recruitment assessment results.

The solution includes:

- ✅ Gradient Boosting as the final machine learning model
- ✅ Feature Engineering (Experience Level & Seniority Tier)
- ✅ Cross Validation for model robustness
- ✅ SHAP Explainability for transparent predictions
- ✅ Streamlit Web Application for recruiter-friendly deployment

### Final Model Performance

| Metric | Score |
|---------|-------|
| F1-Score | **0.999** |
| ROC-AUC | **0.9999** |
| Generalization Gap | **0.0005** |

---

# 📂 Dataset

### Dataset Overview

- **Total Records:** 5,000 Candidates
- **Features:** 15 (after Feature Engineering)

### Candidate Information

- Education Level
- Years of Experience
- Number of Relevant Skills
- Technical Test Score
- Interview Score
- Soft Skill Score
- Internal Referral
- Technical Skills
- Experience Level *(Feature Engineering)*
- Seniority Tier *(Feature Engineering)*

### Target Variable

**Hiring Eligibility**

- **1 = Eligible**
- **0 = Not Eligible**

---

# 🛠 Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- SHAP
- Matplotlib
- Seaborn

### Deployment

- Streamlit

### Explainable AI

- SHAP

---

# 📊 Machine Learning Workflow

```
Business Understanding
        │
        ▼
Data Understanding
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Model Development
        │
        ▼
Model Evaluation
        │
        ▼
Explainable AI (SHAP)
        │
        ▼
Deployment (Streamlit)
```

---

# 💼 Business Value

TalentMatch AI helps organizations by:

- Improving hiring decision consistency
- Supporting recruiters with data-driven recommendations
- Providing transparent AI explanations through SHAP
- Reducing manual evaluation effort
- Increasing recruitment efficiency while maintaining human control over the final hiring decision

---

# 🚀 Live Demo

🌐 **Streamlit Application**

> *https://candidatequalityprediction-dataqueens.streamlit.app/*

---

# 📁 Repository Structure

```
TalentMatch-AI/
│
├── data/
│
├── notebooks/
│
├── models/
│
├── deployment/
│   ├── app.py
│   ├── predict.py
│   ├── requirements.txt
│
├── assets/
│
├── README.md
│
└── LICENSE
```

---

# 🔮 Future Improvements

Future enhancements may include:

- Integration with Applicant Tracking Systems (ATS)
- Candidate prediction history and recruitment logs
- Periodic model retraining using new recruitment data
- Model monitoring and fairness evaluation
- Additional recruitment attributes to improve recommendation quality

---

# 📌 Project Highlights

- 🤖 AI-Assisted Hiring Decision Support
- 📈 Gradient Boosting Machine Learning Model
- 🔍 Explainable AI using SHAP
- 🌐 Interactive Streamlit Dashboard
- 💼 Business-Oriented Recruitment Solution

---

# 👥 Team

**Data Queens**

Final Project — Rakamin Academy 

---
