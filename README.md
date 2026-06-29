# Digital Inclusion Pilot - Python Learning Portfolio

## 📌 Research Topic
**Digital Inclusion, Social Equity, and the Governance of the Urban Poor in Guangzhou's Smart City-Driven Regeneration**

This repository documents my Python learning journey for my proposed phd proposal

---

## 📊 1. Policy Analysis → Problem Statement

Using Python to analyze Guangzhou's urban renewal and smart community policies across three Five-Year Plan periods (13th–15th), I found:

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

### 3.1 Quantitative: Survey

| Tool | What it does | Validation | Code |
| :--- | :--- | :--- | :--- |
| **Poverty Screening** | Identify urban poor (6 dimensions) | KR-20 + Expert Review + Theory Alignment | `poverty_screening_validation.py` |
| **Likert Scales** | Measure barriers and competencies | Cronbach's α | `likert_reliability.py` |

#### 3.2 Qualitative: Interview

| Tool | What it does | Code |
| :--- | :--- | :--- |
| **Word Cloud** | Extract keywords from interview transcripts | `interview_wordcloud.py` |

---

## 📋 4. Poverty Screening Table Validation

### 4.1 Six Dimensions

| Dimension | Source | Measurement |
| :--- | :--- | :--- |
| Income | MPI (UNDP) | Below 1300 RMB/month |
| Education | MPI (UNDP) | High school or below |
| Health | MPI (UNDP) | Age ≥60 or disability |
| Living Standard | MPI (UNDP) | Crowded housing or lack of facilities |
| Digital Skills | Digital Inclusion Literature | Cannot use smartphone independently |
| Non-Guangzhou Hukou | Urban-rural disparity research | Hukou not in Guangzhou |

**Poverty Rule**: ≥2 out of 6 dimensions → classified as urban poor.

### 4.2 Validation Methods

| Method | Result | Interpretation |
| :--- | :--- | :--- |
| **KR-20** (Internal consistency) | 0.125 | Low but acceptable for multidimensional poverty index |
| **Expert Review** (Content validity) | 2-3 experts agreed | Dimensions cover urban poverty characteristics |
| **Theory Alignment** (Construct validity) | Matches UNDP MPI + literature | Each dimension has academic support |

**Conclusion**: The poverty screening table is valid for identifying urban poor in Guangzhou's smart regeneration context.

---

## 📊 5. Likert Scale Reliability Test

Two independent Likert scales (1-5 points):

| Scale | Items | Cronbach's α | Grade |
| :--- | :--- | :--- | :--- |
| **Digital Barriers** (RO1) | 3 items | 0.782 | ✅ Good |
| **Digital Competencies** (RO2/RO3) | 4 items | 0.897 | ✅ Good |

![Likert Scale Reliability](likert_reliability.png)

**Conclusion**: Both scales have good internal consistency and reliably measure digital inclusion perception.

---

## 📂 Repository Files

| File | Role |
| :--- | :--- |
| `poverty_screening_validation.py` | KR-20 validation |
| `likert_reliability.py` | Likert scale reliability |
| `likert_reliability.png` | Reliability chart |
| `policy_analysis.py` | Policy trend analysis |
| `policy_trend_chart.png` | Trend chart |
| `interview_wordcloud.py` | Interview word cloud |
| `interview_wordcloud.png` | Word cloud image |

---

## 🔗 GitHub Repository
[https://github.com/Hzx0402/digitalinclusion-pilot](https://github.com/Hzx0402/digitalinclusion-pilot)
