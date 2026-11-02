import pandas as pd
from prophet import Prophet


class ForecastEngine:

    def __init__(self, dataframe, date_column, value_column):
        self.df = dataframe.copy()
        self.date_column = date_column
        self.value_column = value_column

    def prepare_data(self):
        """
        Prepare data for Prophet.
        Prophet expects columns named:
        ds -> Date
        y  -> Value
        """

        forecast_df = self.df[[self.date_column, self.value_column]].copy()

        forecast_df.columns = ["ds", "y"]

        forecast_df["ds"] = pd.to_datetime(forecast_df["ds"])

        forecast_df = forecast_df.sort_values("ds")

        forecast_df = forecast_df.dropna()

        return forecast_df

    def train_model(self):

        data = self.prepare_data()

        model = Prophet()

        model.fit(data)

        return model

    def generate_forecast(self, periods=30):

        model = self.train_model()

        future = model.make_future_dataframe(periods=periods)

        forecast = model.predict(future)

        return forecast