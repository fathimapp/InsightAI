import pandas as pd


def calculate_metrics(df):
    """Calculate basic dataset metrics."""

    total_rows = len(df)
    total_columns = len(df.columns)

    numeric_columns = len(
        df.select_dtypes(include=["number"]).columns
    )

    missing_values = int(df.isnull().sum().sum())

    duplicates = int(df.duplicated().sum())

    health_score = 100

    health_score -= min(missing_values * 2, 40)
    health_score -= min(duplicates * 5, 30)

    health_score = max(0, health_score)

    return {
        "rows": total_rows,
        "columns": total_columns,
        "numeric_columns": numeric_columns,
        "missing_values": missing_values,
        "duplicates": duplicates,
        "health_score": health_score,
    }