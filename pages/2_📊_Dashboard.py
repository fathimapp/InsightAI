import streamlit as st

from utils.session_manager import get_dataframe
from utils.chart_options import (
    get_all_columns,
    get_numeric_columns,
    get_chart_types
)
from utils.charts import ChartBuilder

st.set_page_config(
    page_title="Visual Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Visual Analytics")
st.caption("Explore your data through interactive visualizations and uncover meaningful business insights.")

# -----------------------------------
# Load Dataset
# -----------------------------------

df = get_dataframe()

if df is None:
    st.warning("⚠️ Please upload a dataset first.")
    st.stop()

st.success("✅ Dataset Loaded Successfully")

st.divider()

# -----------------------------------
# Dataset Overview
# -----------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", len(df))

with col2:
    st.metric("Columns", len(df.columns))

with col3:
    st.metric("Numeric Columns", len(df.select_dtypes(include="number").columns))

st.divider()

# -----------------------------------
# Interactive Chart Builder
# -----------------------------------

st.subheader("📊 Interactive Chart Builder")

chart_type = st.selectbox(
    "Chart Type",
    get_chart_types()
)

all_columns = get_all_columns(df)
numeric_columns = get_numeric_columns(df)

x_axis = st.selectbox(
    "X-Axis",
    all_columns
)

y_axis = None

if chart_type not in ["Histogram", "Pie"]:

    y_axis = st.selectbox(
        "Y-Axis",
        numeric_columns
    )

builder = ChartBuilder(df)

figure = builder.create(
    chart_type,
    x_axis,
    y_axis
)

if figure is not None:
    st.plotly_chart(
        figure,
        use_container_width=True
    )

st.divider()

# -----------------------------------
# Dataset Preview
# -----------------------------------

st.subheader("📋 Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.divider()

# -----------------------------------
# Dataset Information
# -----------------------------------

st.subheader("📑 Column Information")

column_info = (
    df.dtypes.astype(str)
    .reset_index()
    .rename(columns={
        "index": "Column",
        0: "Data Type"
    })
)

st.dataframe(
    column_info,
    use_container_width=True
)