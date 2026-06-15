import streamlit as st
import json
import pandas as pd
import subprocess
import os

st.set_page_config(page_title="Test Coverage Dashboard", layout="wide")

st.title("📊 Test Coverage Dashboard (Real Coverage Analysis)")
st.markdown("Analyze pytest + coverage.py results visually like a mini SonarQube 🚀")

# =========================
# 🔄 RUN COVERAGE BUTTON
# =========================
if st.button("🔄 Run Tests & Generate Coverage"):
    with st.spinner("Running tests and generating coverage..."):
        subprocess.run("coverage run -m pytest", shell=True)
        subprocess.run("coverage json -o coverage.json", shell=True)

    st.success("Coverage updated successfully!")
    st.rerun()

# =========================
# 📂 LOAD COVERAGE DATA
# =========================
if not os.path.exists("coverage.json"):
    st.warning("No coverage.json found. Run tests first using the button above.")
    st.stop()

with open("coverage.json") as f:
    cov_data = json.load(f)

# =========================
# 📊 EXTRACT DATA
# =========================
files = []
coverage_values = []

for file, data in cov_data["files"].items():
    percent = data["summary"]["percent_covered"]
    files.append(file)
    coverage_values.append(percent)

df = pd.DataFrame({
    "File": files,
    "Coverage (%)": coverage_values
})

# =========================
# 📌 METRICS
# =========================
st.subheader("📌 Summary Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Files", len(df))
col2.metric("Avg Coverage", f"{df['Coverage (%)'].mean():.2f}%")
col3.metric("Lowest Coverage", f"{df['Coverage (%)'].min():.2f}%")

# =========================
# 📊 TABLE VIEW
# =========================
st.subheader("📁 Coverage Table")
st.dataframe(df.sort_values("Coverage (%)", ascending=False))

# =========================
# 📊 CHART
# =========================
st.subheader("📊 Coverage Visualization")
st.bar_chart(df.set_index("File"))

# =========================
# 🚨 RISK ANALYSIS
# =========================
st.subheader("🚨 Risk Analysis")

high_risk = df[df["Coverage (%)"] < 50]
medium_risk = df[(df["Coverage (%)"] >= 50) & (df["Coverage (%)"] < 70)]

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔴 High Risk (<50%)")
    if high_risk.empty:
        st.success("No high-risk files 🎉")
    else:
        for _, row in high_risk.iterrows():
            st.error(f"{row['File']} → {row['Coverage (%)']}%")

with col2:
    st.markdown("### 🟡 Medium Risk (50–70%)")
    if medium_risk.empty:
        st.success("No medium-risk files 🎉")
    else:
        for _, row in medium_risk.iterrows():
            st.warning(f"{row['File']} → {row['Coverage (%)']}%")

# =========================
# 📥 DOWNLOAD REPORT
# =========================
st.subheader("📥 Export Report")

csv = df.to_csv(index=False)

st.download_button(
    label="Download Coverage Report (CSV)",
    data=csv,
    file_name="coverage_report.csv",
    mime="text/csv"
)