import streamlit as st

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
load_css()

st.set_page_config(
    page_title="InsightAI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 InsightAI")
st.subheader("AI-Powered Business Intelligence Platform")

st.markdown("---")

st.markdown("""
## 👋 Welcome

InsightAI is an AI-powered Business Intelligence platform designed to help businesses analyze their datasets effortlessly.

### 🚀 Features

- 📂 Upload CSV & Excel datasets
- 🧹 Automatic Data Cleaning
- 📊 Interactive Dashboards
- 📈 Business Analytics
- 🤖 AI Business Insights (Groq)
- 📉 Sales Forecasting
- 📄 Export Reports

---

### 👈 Use the navigation menu on the left to begin.

Start by opening **Upload Data** from the sidebar.
""")

st.info("This project is built using Streamlit, Pandas, Plotly, Scikit-learn and Groq AI.")