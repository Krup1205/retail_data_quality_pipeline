import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Retail Dashboard", layout="wide")

st.title("📊 Retail Data Quality Dashboard")

# ==============================
# LOAD MAIN DATA
# ==============================
if not os.path.exists("data/processed/cleaned_retail_data.csv"):
    st.error("⚠️ Run main.py first to generate data")
    st.stop()

df = pd.read_csv("data/processed/cleaned_retail_data.csv", parse_dates=['Date'])

# ==============================
# LOAD RCA DATA
# ==============================
rca_path = "outputs/reports/anomaly_report.csv"

if os.path.exists(rca_path):
    rca_df = pd.read_csv(rca_path, parse_dates=['Date'])

    # Ensure correct type
    rca_df['Store'] = rca_df['Store'].astype(int)
else:
    rca_df = pd.DataFrame()

# ==============================
# STORE SELECTION (SMART UX)
# ==============================
view_option = st.sidebar.radio(
    "Select View",
    ["Only Stores with Anomalies", "All Stores"]
)

if not rca_df.empty and view_option == "Only Stores with Anomalies":
    store_ids = sorted(rca_df['Store'].unique())
else:
    store_ids = sorted(df['Store'].unique())

selected_store = st.sidebar.selectbox("Select Store", store_ids)

store_df = df[df['Store'] == selected_store].sort_values(by='Date')

# ==============================
# KPI METRICS
# ==============================
col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(store_df))
col2.metric("Z-score Anomalies", store_df['is_anomaly'].sum())
col3.metric("Isolation Forest Anomalies", store_df['iforest_anomaly'].sum())

# ==============================
# WARNING IF NO ANOMALY
# ==============================
if not rca_df.empty and selected_store not in rca_df['Store'].values:
    st.warning("⚠️ This store has no detected anomalies")

# ==============================
# SALES PLOT
# ==============================
st.subheader("📈 Sales Trend with Anomalies")

fig, ax = plt.subplots(figsize=(12,5))

ax.plot(store_df['Date'], store_df['Sales'], label='Sales')

z_anom = store_df[store_df['is_anomaly'] == True]
ax.scatter(z_anom['Date'], z_anom['Sales'], label='Z-score', marker='x')

if_anom = store_df[store_df['iforest_anomaly'] == 1]
ax.scatter(if_anom['Date'], if_anom['Sales'], label='IForest', marker='o')

ax.legend()
ax.set_title("Sales with Anomaly Detection")

st.pyplot(fig)

# ==============================
# RCA SECTION
# ==============================
st.subheader("🧠 Root Cause Analysis")

if not rca_df.empty:

    store_rca = rca_df[rca_df['Store'] == selected_store]

    if len(store_rca) == 0:
        st.info("No RCA data for this store")
    else:
        st.dataframe(store_rca.sort_values(by="Sales", ascending=False))

else:
    st.warning("⚠️ RCA file not found. Run main.py")

# ==============================
# DETAILED RCA VIEW
# ==============================
st.subheader("🔍 Detailed RCA View")

if not rca_df.empty and len(store_rca) > 0:

    selected_row = st.selectbox(
        "Select anomaly date",
        store_rca['Date']
    )

    detail = store_rca[store_rca['Date'] == selected_row].iloc[0]

    st.write(f"**Store:** {detail['Store']}")
    st.write(f"**Date:** {detail['Date']}")
    st.write(f"**Sales:** {detail['Sales']}")
    st.write(f"**Type:** {detail['AnomalyType']}")

    st.write("### Reasons:")

    reasons = str(detail['Reasons']).split(";")
    for r in reasons:
        st.write(f"- {r.strip()}")

else:
    st.info("Select a store with anomalies")

# ==============================
# DEBUG PANEL (REMOVE LATER)
# ==============================
with st.expander("🔧 Debug Info"):
    st.write("Selected Store:", selected_store)
    st.write("RCA Rows:", len(rca_df))
    if not rca_df.empty:
        st.write("RCA Stores:", rca_df['Store'].unique()[:10])