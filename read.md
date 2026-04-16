# 📊 Retail Data Quality Monitoring System

An end-to-end data pipeline that simulates real-world FMCG retail data operations, performing automated anomaly detection, root cause analysis (RCA), and reporting — inspired by production systems like NielsenIQ’s Consumer Information Platform (CIP).

---

## 🚀 Project Overview

This project goes beyond a typical machine learning model by implementing a **complete data operations pipeline**, including:

* Data ingestion from multiple sources
* Data validation and cleaning
* Statistical and ML-based anomaly detection
* Root cause analysis (RCA)
* Automated reporting
* Interactive dashboard for insights

---

## 🔥 Key Features

### 🔄 Data Ingestion & Validation

* Multi-source data merging (`train.csv` + `store.csv`)
* Missing value detection and handling
* Business rule validation (e.g., zero sales when store is open)

---

### 🧹 Data Preprocessing

* Domain-aware missing value imputation
* Feature engineering (date-based features)
* Removal of irrelevant records (closed stores)

---

### 📊 Anomaly Detection

#### 1. Statistical Method — Z-Score

* Detects spikes and drops in sales
* Store-level normalization

#### 2. Machine Learning — Isolation Forest

* Multivariate anomaly detection
* Uses:

  * Sales
  * Customers
  * Promotions
  * Competition

---

### 🧠 Root Cause Analysis (RCA)

* Rule-based explanation engine
* Context-aware reasoning (Spike vs Drop)

Examples:

* 📈 Sales spike → Promotion / high demand
* 📉 Sales drop → No promotion / low customers
* 🛑 Zero customers → Possible store issue

---

### 📄 Automated Reporting

* Generates structured reports:

  * CSV
  * Excel
* Includes:

  * Store
  * Date
  * Sales
  * Anomaly Type
  * RCA Explanation

---

### 📈 Interactive Dashboard (Streamlit)

* Store-level filtering
* KPI metrics
* Sales trend visualization
* Anomaly highlighting
* RCA drill-down view

---

## 🏗️ Architecture

```
Data Sources
     ↓
Ingestion Layer
     ↓
Validation Layer
     ↓
Data Cleaning
     ↓
Anomaly Detection (Z-score + Isolation Forest)
     ↓
Root Cause Analysis (RCA)
     ↓
Report Generation
     ↓
Streamlit Dashboard
```

---

## ⚙️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn (Isolation Forest)**
* **Matplotlib**
* **Streamlit**
* **Great Expectations (optional for validation)**

---

## 📂 Project Structure

```
retail-data-quality-pipeline/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── src/
│   ├── ingestion/
│   ├── validation/
│   ├── preprocessing/
│   ├── anomaly_detection/
│   ├── rca/
│   ├── reporting/
│
├── outputs/
│   ├── reports/
│
├── app/
│   └── dashboard.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Clone Repository

```
git clone <your-repo-link>
cd retail-data-quality-pipeline
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Run Pipeline

```
python main.py
```

---

### 4. Run Dashboard

```
streamlit run app/dashboard.py
```

---

## 📊 Sample Insights

* Detected anomalies across multiple retail stores
* Identified causes such as:

  * Promotion-driven sales spikes
  * Stock-out or operational issues
  * Customer inactivity

---

## 💡 Key Highlights

* Built a **production-style data pipeline**, not just an ML model
* Combined **statistical + machine learning approaches**
* Added **business-level explainability (RCA)**
* Developed **end-to-end system from ingestion to dashboard**

---

## 🚀 Future Improvements

* SHAP-based explainability (advanced RCA)
* Real-time anomaly detection
* Alert system (Email/Slack notifications)
* Deployment on cloud (Render / AWS / Railway)

---

## 🧠 Learning Outcomes

* Data pipeline design
* Data validation and cleaning strategies
* Anomaly detection techniques
* Explainable AI (RCA concepts)
* Dashboard development

---

## 👨‍💻 Author

**Krup Patel**
Aspiring Data Scientist / AI-ML Engineer

---

## ⭐ Final Note

This project demonstrates how to build a **real-world data quality monitoring system**, going beyond traditional ML projects by integrating data engineering, machine learning, and business intelligence.

---
