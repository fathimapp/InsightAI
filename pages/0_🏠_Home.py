import streamlit as st

st.set_page_config(
    page_title="InsightAI",
    page_icon="📊",
    layout="wide"
)

# =========================
# HERO SECTION
# =========================

st.markdown("""
<style>

.hero{
    background:linear-gradient(135deg,#2563EB,#1E3A8A);
    padding:55px;
    border-radius:22px;
    color:white;
    text-align:center;
    margin-bottom:30px;
    box-shadow:0px 12px 35px rgba(0,0,0,0.15);
}

.hero h1{
    font-size:55px;
    margin-bottom:10px;
    color:white;
}

.hero h3{
    color:#E2E8F0;
    font-weight:400;
}

.hero p{
    font-size:18px;
    color:#F8FAFC;
}

.stat-card{
    background:white;
    border-radius:18px;
    padding:25px;
    text-align:center;
    box-shadow:0 8px 20px rgba(0,0,0,.08);
    border:1px solid #E5E7EB;
    color:#1E293B;
}

.stat-card h2{
    color:#2563EB;
    font-size:42px;
    margin-bottom:8px;
}

.stat-card p{
    color:#64748B;
    font-size:16px;
    font-weight:600;
}

.feature-card{
    background:white;
    border-radius:18px;
    padding:25px;
    box-shadow:0 8px 20px rgba(0,0,0,.08);
    border:1px solid #E5E7EB;
    height:260px;
    color:#1E293B;
}

.feature-card h3{
    color:#2563EB;
    margin-bottom:15px;
}

.feature-card p{
    color:#475569;
    font-size:16px;
    line-height:1.7;
}

.feature-card ul{
    color:#475569;
    margin-top:15px;
}

.feature-card li{
    margin-bottom:10px;
}

.feature-card h3{
    color:#2563EB;
}

.tech{
    .tech{
    background:#EFF6FF;
    color:#1E293B;
    padding:18px;
    border-radius:15px;
    text-align:center;
    font-size:18px;
    font-weight:700;
    border:1px solid #BFDBFE;

}

.footer{
    text-align:center;
    color:gray;
    padding:30px;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<h1>📊 InsightAI</h1>

<h3>AI-Powered Business Intelligence Platform</h3>

<p>
Transform raw business data into intelligent insights using Artificial Intelligence,
interactive analytics, forecasting, and automated reporting.
</p>

</div>
""", unsafe_allow_html=True)

# =========================
# PLATFORM STATS
# =========================

st.markdown("## 📈 Platform Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="stat-card">
    <h2>6</h2>
    <p>Core Modules</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="stat-card">
    <h2>AI</h2>
    Powered
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="stat-card">
    <h2>ML</h2>
    Forecasting
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="stat-card">
    <h2>100%</h2>
    Interactive
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =========================
# FEATURES
# =========================

st.markdown("## 🚀 Platform Modules")

a, b, c = st.columns(3)

with a:
    st.markdown("""
<div class="feature-card">

<h3>📂 Upload Data</h3>

<p>
Upload CSV and Excel datasets securely.
</p>

<ul>
<li>Automatic Preview</li>
<li>Data Validation</li>
<li>Generic Dataset Support</li>
</ul>

</div>
""", unsafe_allow_html=True)

with b:
    st.markdown("""
<div class="feature-card">

<h3>📊 Executive Dashboard</h3>

Interactive KPIs and visual analytics.

<br>

✔ KPIs

✔ Charts

✔ Business Metrics

</div>
""", unsafe_allow_html=True)

with c:
    st.markdown("""
<div class="feature-card">

<h3>🤖 AI Business Analyst</h3>

Generate intelligent business insights.

<br>

✔ Executive Summary

✔ Risks

✔ Recommendations

</div>
""", unsafe_allow_html=True)

st.write("")

d, e, f = st.columns(3)

with d:
    st.markdown("""
<div class="feature-card">

<h3>📈 Visual Analytics</h3>

Explore data using professional charts.

<br>

✔ Pie Charts

✔ Bar Charts

✔ Scatter Plots

</div>
""", unsafe_allow_html=True)

with e:
    st.markdown("""
<div class="feature-card">

<h3>📉 AI Forecasting</h3>

Predict future business trends.

<br>

✔ Linear Regression

✔ Forecast Models

✔ Trend Analysis

</div>
""", unsafe_allow_html=True)

with f:
    st.markdown("""
<div class="feature-card">

<h3>📄 AI Report Center</h3>

Generate professional reports.

<br>

✔ Export Ready

✔ Business Reports

✔ Executive Format

</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# TECHNOLOGY
# =========================

st.markdown("## 🛠 Technology Stack")

t1, t2, t3, t4, t5, t6 = st.columns(6)

with t1:
    st.markdown('<div class="tech">Python</div>', unsafe_allow_html=True)

with t2:
    st.markdown('<div class="tech">Streamlit</div>', unsafe_allow_html=True)

with t3:
    st.markdown('<div class="tech">Pandas</div>', unsafe_allow_html=True)

with t4:
    st.markdown('<div class="tech">Plotly</div>', unsafe_allow_html=True)

with t5:
    st.markdown('<div class="tech">Groq AI</div>', unsafe_allow_html=True)

with t6:
    st.markdown('<div class="tech">Prophet</div>', unsafe_allow_html=True)

st.write("")

# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">

<hr>

<b>InsightAI v1.0</b><br>

AI-Powered Business Intelligence Platform

<br><br>

Built with ❤️ using Python • Streamlit • Plotly • Groq • Prophet

</div>
""", unsafe_allow_html=True)