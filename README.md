# Digital Inclusion Pilot - Python Learning Portfolio

## 📌 Research Topic
**Digital Inclusion, Social Equity, and the Governance of the Urban Poor in Guangzhou's Smart City-Driven Regeneration**

This repository documents my Python learning journey for my proposed PhD research under **Prof. Xiang Lv** at HKUST(GZ).

---

## 📊 1. Policy Analysis → Problem Statement

Using Python to analyze Guangzhou's urban regeneration and smart community policies across three Five-Year Plan periods (13th–15th), I found:

| Keyword Category | 13th FYP | 14th FYP | 15th FYP | Change |
| :--- | :--- | :--- | :--- | :--- |
| Spatial Renewal | 32.89 | 6.44 | 1.61 | ↓ 95% |
| Technological Empowerment | 0.00 | 7.68 | 3.33 | ↑ then ↓ |
| Participatory Fairness | 1.53 | 0.28 | 0.14 | ↓ 91% |
| Care for Vulnerable Groups | 0.49 | 0.56 | 1.76 | ↑ 259% |

**The Problem**: Policy focuses more on technology but less on fair participation. At the same time, it shows more "care" for vulnerable groups without emphasizing their "participation." This raises a critical question: **Are vulnerable groups being cared for or being silenced in smart city regeneration?**

---

## ❓ 2. Research Questions

| RO | Question |
| :--- | :--- |
| RO1 | What specific access barriers do the urban poor face when encountering and using the digital governance tools within smart regeneration projects?|
| RO2 | What impact do digitalised governance and services have on the core capabilities of the urban poor, such as community participation, information access, and social networks? |
| RO3 | Overall, is Guangzhou's smart regeneration model bridging or exacerbating existing social inequalities? |

---

## 🛠 3. Research Design

### Quantitative: Survey

| Tool | What it does | Validation | Code |
| :--- | :--- | :--- | :--- |
| **Poverty Screening** | Identify urban poor groups (4 dimensions: economy, migration, physiology, education) | Logistic regression + Chi-square + 100% accuracy | `poverty_screening_validation.py` |
| **Likert Scale** | Measure digital inclusion perception (7 items: barriers + competencies) | Cronbach's α = 0.78 / 0.90 | `likert_reliability.py` |

### Qualitative: Interview

| Tool | What it does | Code |
| :--- | :--- | :--- |
| **Word Cloud** | Extract keywords from interview transcripts (THULAC segmentation) | `interview_wordcloud.py` |

---

## 📂 Repository Files

| File | What it does | Which RO it supports |
| :--- | :--- | :--- |
| `policy_analysis.py` | Policy trend analysis (identify the problem) | Background |
| `poverty_screening_validation.py` | Identify who are the "urban poor" (screening tool validation) | **Prerequisite for RO1** |
| `likert_reliability.py` | Measure digital inclusion perception (barriers + competencies) | **RO1, RO2, RO3** |
| `interview_wordcloud.py` | Extract keywords from interview transcripts | **Qualitative support for RO1-RO3** |
| `interview_wordcloud.png` | Word cloud: 手机、功能、子女 | **Qualitative evidence** |

---

## 🔗 GitHub Repository
[https://github.com/Hzx0402/digitalinclusion-pilot](https://github.com/Hzx0402/digitalinclusion-pilot)