import pandas as pd


class ColumnDetector:
    """
    Detects useful columns from any uploaded business dataset.
    """

    def __init__(self, df):
        self.df = df
        self.columns = [col.lower().strip() for col in df.columns]

    def find_numeric_columns(self):
        return self.df.select_dtypes(include="number").columns.tolist()

    def find_date_columns(self):
        date_columns = []

        for column in self.df.columns:
            try:
                converted = pd.to_datetime(self.df[column], errors="coerce")

                if converted.notna().sum() > len(self.df) * 0.6:
                    date_columns.append(column)

            except Exception:
                pass

        return date_columns

    def find_categorical_columns(self):
        return self.df.select_dtypes(include=["object", "category"]).columns.tolist()

    def find_sales_column(self):
        keywords = [
            "sales",
            "sale",
            "revenue",
            "amount",
            "income",
            "total"
        ]

        return self._find_column(keywords)

    def find_profit_column(self):
        keywords = [
            "profit",
            "earning",
            "margin",
            "net"
        ]

        return self._find_column(keywords)

    def find_quantity_column(self):
        keywords = [
            "quantity",
            "qty",
            "units"
        ]

        return self._find_column(keywords)

    def find_customer_column(self):
        keywords = [
            "customer",
            "customer name",
            "client"
        ]

        return self._find_column(keywords)

    def find_region_column(self):
        keywords = [
            "region",
            "state",
            "city",
            "country",
            "location"
        ]

        return self._find_column(keywords)

    def find_category_column(self):
        keywords = [
            "category",
            "segment",
            "type"
        ]

        return self._find_column(keywords)

    def _find_column(self, keywords):
        for keyword in keywords:
            for original, lower in zip(self.df.columns, self.columns):
                if keyword in lower:
                    return original

        return None