import streamlit as st
import pandas as pd
import plotly.express as px

from utils.session_manager import get_dataframe
from utils.forecast_engine import ForecastEngine

st.set_page_config(
    page_title="Forecasting",
    page_icon="📉",
    layout="wide"
)

st.title("📉 AI Forecasting Studio")
st.write("Predict future trends using Machine Learning.")

df = get_dataframe()

if df is None:
    st.warning("⚠️ Please upload a dataset first.")
    st.stop()

st.success("✅ Dataset Loaded Successfully")

st.subheader("📋 Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

st.divider()

# -----------------------
# Detect Columns
# -----------------------

date_columns = []

for col in df.columns:
    try:
        pd.to_datetime(df[col])
        date_columns.append(col)
    except:
        pass

numeric_columns = df.select_dtypes(include="number").columns.tolist()

if len(date_columns) == 0:
    st.warning("⚠️ No date column found.")
    st.info("Forecasting requires a valid date column.")
    st.stop()

if len(numeric_columns) == 0:
    st.warning("⚠️ No numeric column found.")
    st.stop()

st.subheader("⚙ Forecast Settings")

date_col = st.selectbox(
    "Select Date Column",
    date_columns
)

value_col = st.selectbox(
    "Select Value Column",
    numeric_columns
)

forecast_days = st.slider(
    "Forecast Days",
    min_value=7,
    max_value=365,
    value=30
)

if st.button("🚀 Generate Forecast", use_container_width=True):

    with st.spinner("Training AI Forecast Model..."):

        try:

            engine = ForecastEngine(
                df,
                date_col,
                value_col
            )

            forecast = engine.generate_forecast(forecast_days)

            st.success("✅ Forecast Generated Successfully")

            st.subheader("📈 Forecast Chart")

            fig = px.line(
                forecast,
                x="ds",
                y="yhat",
                title="Future Forecast"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.subheader("📄 Forecast Table")

            st.dataframe(
                forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]],
                use_container_width=True
            )

            csv = forecast.to_csv(index=False)

            st.download_button(
                "⬇ Download Forecast CSV",
                csv,
                "forecast.csv",
                "text/csv"
            )

        except Exception as e:

            st.error(f"Forecast failed: {e}")