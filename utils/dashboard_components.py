import streamlit as st


def show_kpi_cards(metrics):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📄 Rows",
        f"{metrics['rows']:,}"
    )

    c2.metric(
        "📑 Columns",
        metrics["columns"]
    )

    c3.metric(
        "🔢 Numeric",
        metrics["numeric_columns"]
    )

    c4.metric(
        "💚 Health",
        f"{metrics['health_score']}%"
    )

    c5, c6 = st.columns(2)

    c5.metric(
        "❗ Missing",
        metrics["missing_values"]
    )

    c6.metric(
        "📋 Duplicates",
        metrics["duplicates"]
    )