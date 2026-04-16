📊 Retail Data Quality Monitoring System

An end-to-end data pipeline that simulates FMCG retail data operations, performing automated anomaly detection, root cause analysis (RCA), and reporting — inspired by real-world systems like NielsenIQ’s Consumer Information Platform (CIP).

🚀 Features
🔄 Data Ingestion & Validation
Multi-source data merging
Missing value & data quality checks
🧹 Data Preprocessing
Business-aware cleaning
Feature engineering
📊 Anomaly Detection
Z-score (statistical)
Isolation Forest (ML-based)
🧠 Root Cause Analysis (RCA)
Rule-based explanation engine
Context-aware reasoning (spike/drop detection)
📄 Automated Reporting
CSV & Excel reports
Structured anomaly insights
📈 Interactive Dashboard (Streamlit)
Store-level anomaly visualization
RCA drill-down view
KPI metrics
🏗️ Project Architecture
data → validation → cleaning → anomaly detection → RCA → reporting → dashboard
⚙️ Tech Stack
Python (Pandas, NumPy)
Scikit-learn (Isolation Forest)
Matplotlib
Streamlit
Great Expectations (optional)
📊 Sample Output
Detected anomalies in retail sales patterns
Identified causes like:
Promotion-driven spikes
Stock-out related drops
Customer inactivity
▶️ How to Run
# Step 1: Run pipeline
python main.py

# Step 2: Run dashboard
streamlit run app/dashboard.py
💡 Key Insight

Unlike typical ML projects, this system replicates a full production data loop:

ingestion → validation → anomaly detection → RCA → reporting

🧾 Resume Bullet (Use This EXACTLY)
🔥 Strong Version

Built an end-to-end retail data quality monitoring system with automated anomaly detection (Z-score, Isolation Forest), root cause analysis, and interactive dashboard, simulating real-world FMCG data pipelines.

🔥 Stronger Version (If Space)

Developed a production-style retail data pipeline integrating anomaly detection (statistical & ML), rule-based root cause analysis, and automated reporting with a Streamlit dashboard, improving anomaly diagnosis and business interpretability.
