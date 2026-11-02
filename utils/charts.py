import plotly.express as px


class ChartBuilder:

    def __init__(self, df):
        self.df = df

    def create(self, chart_type, x_column, y_column=None):

        if chart_type == "Bar":
            return px.bar(
                self.df,
                x=x_column,
                y=y_column,
                template="plotly_white"
            )

        elif chart_type == "Line":
            return px.line(
                self.df,
                x=x_column,
                y=y_column,
                template="plotly_white"
            )

        elif chart_type == "Scatter":
            return px.scatter(
                self.df,
                x=x_column,
                y=y_column,
                template="plotly_white"
            )

        elif chart_type == "Histogram":
            return px.histogram(
                self.df,
                x=x_column,
                template="plotly_white"
            )

        elif chart_type == "Box":
            return px.box(
                self.df,
                x=x_column,
                y=y_column,
                template="plotly_white"
            )

        elif chart_type == "Pie":

            pie = (
                self.df.groupby(x_column)
                .size()
                .reset_index(name="Count")
            )

            return px.pie(
                pie,
                names=x_column,
                values="Count"
            )

        return None