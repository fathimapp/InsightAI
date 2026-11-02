import streamlit as st
import pandas as pd


class FilterEngine:
    def __init__(self, df):
        self.df = df.copy()

    def apply(self):
        """
        Automatically creates filters for categorical columns.
        """

        filtered_df = self.df.copy()

        st.sidebar.markdown("## 🔍 Dataset Filters")

        categorical_columns = filtered_df.select_dtypes(
            include=["object", "category"]
        ).columns

        for column in categorical_columns:

            values = sorted(
                filtered_df[column]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

            if len(values) > 25:
                continue

            selected = st.sidebar.multiselect(
                label=column,
                options=values,
                default=values
            )

            filtered_df = filtered_df[
                filtered_df[column]
                .astype(str)
                .isin(selected)
            ]

        return filtered_df