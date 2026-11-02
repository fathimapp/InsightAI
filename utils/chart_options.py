import pandas as pd


def get_numeric_columns(df):
    return df.select_dtypes(include="number").columns.tolist()


def get_all_columns(df):
    return df.columns.tolist()


def get_chart_types():

    return [
        "Bar",
        "Line",
        "Scatter",
        "Histogram",
        "Box",
        "Pie"
    ]