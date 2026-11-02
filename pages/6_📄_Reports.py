import streamlit as st
import pandas as pd

from utils.session_manager import get_dataframe

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Report Center")
st.write("Generate and download professional business reports.")

df = get_dataframe()

if df is None:
    st.warning("⚠️ Please upload a dataset first.")
    st.stop()

st.success("✅ Dataset Loaded Successfully")

# -------------------------
# Dataset Summary
# -------------------------

st.subheader("📊 Dataset Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Rows", len(df))

with col2:
    st.metric("Columns", len(df.columns))

with col3:
    st.metric("Missing", int(df.isnull().sum().sum()))

with col4:
    st.metric("Duplicates", int(df.duplicated().sum()))

st.divider()

# -------------------------
# Preview
# -------------------------

st.subheader("📄 Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

st.divider()

# -------------------------
# Downloads
# -------------------------

st.subheader("⬇ Export Reports")

csv = df.to_csv(index=False)

st.download_button(
    "📄 Download CSV Report",
    csv,
    "dataset_report.csv",
    "text/csv",
    use_container_width=True
)

excel_buffer = pd.ExcelWriter("report.xlsx", engine="openpyxl")
df.to_excel(excel_buffer, index=False)
excel_buffer.close()

with open("report.xlsx", "rb") as file:
    st.download_button(
        "📊 Download Excel Report",
        file,
        "dataset_report.xlsx",
        use_container_width=True
    )

summary = f"""
InsightAI Report

Rows : {len(df)}

Columns : {len(df.columns)}

Missing Values : {df.isnull().sum().sum()}

Duplicate Rows : {df.duplicated().sum()}

Columns

"""

for col in df.columns:
    summary += f"- {col} ({df[col].dtype})\n"

st.download_button(
    "📝 Download Summary Report",
    summary,
    "summary_report.txt",
    use_container_width=True
)