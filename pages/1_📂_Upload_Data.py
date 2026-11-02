import streamlit as st
from utils.file_handler import load_file
from utils.data_cleaner import clean_data
from utils.session_manager import save_dataframe

st.set_page_config(
    page_title="Upload Data",
    page_icon="📂",
    layout="wide"
)

# ======================================
# CUSTOM CSS
# ======================================

st.markdown("""
<style>

.main{
    background-color:#F8FAFC;
}

.hero{
    background:linear-gradient(135deg,#2563EB,#1E3A8A);
    padding:45px;
    border-radius:22px;
    color:white;
    text-align:center;
    margin-bottom:30px;
    box-shadow:0px 10px 30px rgba(0,0,0,0.15);
}

.hero h1{
    font-size:48px;
    margin-bottom:10px;
    color:white;
}

.hero h4{
    color:#E2E8F0;
    font-weight:400;
}

.hero p{
    font-size:18px;
    color:white;
}

.upload-box{
    background:white;
    padding:35px;
    border-radius:20px;
    border:2px dashed #2563EB;
    text-align:center;
    box-shadow:0px 8px 20px rgba(0,0,0,0.08);
    margin-bottom:25px;
}

.card{
    background:white;
    border-radius:18px;
    padding:20px;
    text-align:center;
    box-shadow:0px 8px 18px rgba(0,0,0,0.08);
    border:1px solid #E5E7EB;
}

.card h2{
    color:#2563EB;
    margin-bottom:5px;
}

.card p{
    color:#475569;
    font-size:15px;
}

.section-title{
    font-size:28px;
    font-weight:700;
    color:#1E293B;
    margin-top:15px;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ======================================
# HERO
# ======================================

st.markdown("""
<div class="hero">

<h1>📂 Upload Dataset</h1>

<h4>Securely upload your business datasets</h4>

<p>
Upload CSV or Excel files and let InsightAI automatically
clean, analyze and prepare your data for AI-powered insights.
</p>

</div>
""", unsafe_allow_html=True)

# ======================================
# UPLOAD AREA
# ======================================

st.markdown("""
<div class="upload-box">

<h2 style="color:#2563EB;">
📁 Select Your Dataset
</h2>

<p style="color:#64748B;font-size:17px;">
Supported formats:
<b>CSV</b>,
<b>XLSX</b>

</p>

</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "",
    type=["csv","xlsx"]
)

# ======================================
# BEFORE UPLOAD
# ======================================

if uploaded_file is None:

    st.info("👆 Upload a dataset to begin your AI-powered business analysis.")

    st.markdown("<div class='section-title'>🚀 Why Upload with InsightAI?</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
<div class="card">

<h2>⚡</h2>

<p><b>Automatic Cleaning</b></p>

Removes duplicate rows and prepares your dataset automatically.

</div>
""", unsafe_allow_html=True)

    with c2:
        st.markdown("""
<div class="card">

<h2>🤖</h2>

<p><b>AI Ready</b></p>

Your dataset becomes instantly available for AI Insights,
Forecasting and Reports.

</div>
""", unsafe_allow_html=True)

    with c3:
        st.markdown("""
<div class="card">

<h2>📊</h2>

<p><b>Interactive Analytics</b></p>

Generate dashboards and professional visualizations
with one click.

</div>
""", unsafe_allow_html=True)

    st.stop()

# ======================================
# LOAD DATA
# ======================================

df = load_file(uploaded_file)

if df is not None:

    df, duplicates, missing = clean_data(df)

    save_dataframe(df)

    st.success("✅ Dataset uploaded successfully!")

    st.markdown("<div class='section-title'>📊 Dataset Overview</div>", unsafe_allow_html=True)

    r1, r2, r3, r4 = st.columns(4)

    with r1:
        st.markdown(f"""
<div class="card">
<h2>{df.shape[0]}</h2>
<p>Rows</p>
</div>
""", unsafe_allow_html=True)

    with r2:
        st.markdown(f"""
<div class="card">
<h2>{df.shape[1]}</h2>
<p>Columns</p>
</div>
""", unsafe_allow_html=True)

    with r3:
        st.markdown(f"""
<div class="card">
<h2>{missing}</h2>
<p>Missing Values</p>
</div>
""", unsafe_allow_html=True)

    with r4:
        st.markdown(f"""
<div class="card">
<h2>{duplicates}</h2>
<p>Duplicates Removed</p>
</div>
""", unsafe_allow_html=True)


    st.markdown("<div class='section-title'>📁 File Information</div>", unsafe_allow_html=True)

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown(f"""
<div class="card">
<h2>📄</h2>
<p><b>Filename</b></p>
{uploaded_file.name}
</div>
""", unsafe_allow_html=True)

    with f2:
        size = round(uploaded_file.size / 1024, 2)

        st.markdown(f"""
<div class="card">
<h2>💾</h2>
<p><b>File Size</b></p>
{size} KB
</div>
""", unsafe_allow_html=True)

    with f3:
        extension = uploaded_file.name.split(".")[-1].upper()

        st.markdown(f"""
<div class="card">
<h2>📑</h2>
<p><b>Format</b></p>
{extension}
</div>
""", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>❤️ Data Health</div>", unsafe_allow_html=True)

    total_cells = df.shape[0] * df.shape[1]

    if total_cells == 0:
        health = 100
    else:
        health = max(
            0,
            round(
                100 - ((missing / total_cells) * 100),
                1
            )
        )

    st.progress(int(health))

    if health >= 95:
        st.success(f"Excellent Dataset Quality • {health}%")

    elif health >= 80:
        st.warning(f"Good Dataset Quality • {health}%")

    else:
        st.error(f"Poor Dataset Quality • {health}%")

    st.markdown("<div class='section-title'>📋 Dataset Preview</div>", unsafe_allow_html=True)

    st.dataframe(
        df,
        use_container_width=True,
        height=450
    )

    st.markdown("<div class='section-title'>📑 Column Information</div>", unsafe_allow_html=True)

    info = df.dtypes.astype(str).reset_index()

    info.columns = ["Column", "Data Type"]

    st.dataframe(
        info,
        use_container_width=True
    )

    st.markdown("<div class='section-title'>📊 Dataset Statistics</div>", unsafe_allow_html=True)

    numeric_df = df.select_dtypes(include="number")

    if not numeric_df.empty:
        st.dataframe(
            numeric_df.describe(),
            use_container_width=True
        )

    st.success("🚀 Your dataset is ready for Executive Dashboard, Visual Analytics, AI Insights, Forecasting and Reports.")

    c1, c2 = st.columns(2)

    with c1:
        st.info("""
### ✅ Next Step

Go to **Executive Dashboard**

Explore KPIs

Interactive Charts

Business Metrics
""")

    with c2:
        st.info("""
### 🤖 AI Ready

Your dataset has been saved.

You can now use

• AI Business Analyst

• Forecasting

• Report Center
""")

    st.markdown("---")

    st.markdown(
        """
<div style="text-align:center;color:gray;padding:20px;">

<b>InsightAI Upload Center</b>

<br>

Enterprise Secure Dataset Management

</div>
""",
        unsafe_allow_html=True
)