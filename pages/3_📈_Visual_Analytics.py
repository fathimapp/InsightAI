import streamlit as st

from utils.session_manager import get_dataframe
from utils.chart_options import (
    get_all_columns,
    get_numeric_columns,
    get_chart_types
)
from utils.charts import ChartBuilder

st.set_page_config(
    page_title="Analytics Studio",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Analytics Studio")
st.caption("Create interactive visualizations from any dataset")

df = get_dataframe()

if df is None:
    st.warning("Please upload a dataset first.")
    st.stop()

st.sidebar.header("Chart Configuration")

chart_type = st.sidebar.selectbox(
    "Chart Type",
    get_chart_types()
)

x_axis = st.sidebar.selectbox(
    "X-Axis",
    get_all_columns(df)
)

y_axis = None

if chart_type not in ["Histogram", "Pie"]:
    y_axis = st.sidebar.selectbox(
        "Y-Axis",
        get_numeric_columns(df)
    )

builder = ChartBuilder(df)

fig = builder.create(
    chart_type,
    x_axis,
    y_axis
)

if fig:
    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Dataset Preview")

st.dataframe(
    df,
    use_container_width=True
)