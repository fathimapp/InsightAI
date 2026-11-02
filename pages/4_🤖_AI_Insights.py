import streamlit as st
from dotenv import load_dotenv
import os

from utils.session_manager import get_dataframe
from utils.ai_engine import AIEngine

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="AI Insights",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Business Analyst")
st.write("Generate AI-powered business insights from your uploaded dataset.")

# Load dataset
df = get_dataframe()

if df is None:
    st.warning("⚠️ Please upload a dataset first.")
    st.stop()

# Get API Key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ_API_KEY not found in your .env file.")
    st.stop()

# Dataset Summary
st.subheader("📋 Dataset Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", len(df))

with col2:
    st.metric("Columns", len(df.columns))

with col3:
    st.metric("Missing Values", int(df.isnull().sum().sum()))

st.divider()

# Dataset Preview
st.subheader("📄 Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

st.divider()

# Generate AI Insights
if st.button("🤖 Generate AI Insights", use_container_width=True):

    with st.spinner("🧠 AI is analyzing your dataset..."):

        try:
            ai = AIEngine(api_key)
            result = ai.analyze_dataset(df)

            st.success("✅ Analysis Completed")

            st.markdown("## 📊 AI Business Report")
            st.markdown(result)

        except Exception as e:
            st.error(f"❌ Error: {e}")