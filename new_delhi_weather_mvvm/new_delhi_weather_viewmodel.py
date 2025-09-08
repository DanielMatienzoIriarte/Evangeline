from PyQt6.QtCore import QObject, pyqtSignal
from pandas.core.interchange.dataframe_protocol import DataFrame
from plotly.graph_objs import Figure
from prophet import Prophet
from prophet.plot import plot_plotly
# research PyQtGraph instead of matplotlib

from new_delhi_weather_mvvm.new_delhi_weather_model import NewDelhiWeather as model


class NewDelhiWeather(QObject):
    graphic_updated = pyqtSignal(Figure)

    def __init__(self, model: model, parent=None):
        super().__init__()

        self._predictions = None
        self._forecast_periods = 700
        self._model = model

        self._forecaster_model = Prophet()
        self._forecast_data = self._model.get_data().rename(columns={"date": "ds", "meantemp": "y"})

    """
    Generates a weather forecast prediction.
    
    returns:
        A matplotlib figure
    """
    def generate_prediction(self)->Figure:
        # print(self.forecast_data)
        self._forecaster_model.fit(self._forecast_data)
        forecasts = self._forecaster_model.make_future_dataframe(periods=self._forecast_periods)
        predictions = self._forecaster_model.predict(forecasts)

# TODO thiis is what I have to emit 
        figure = plot_plotly(self._forecaster_model, predictions)
        return figure

    """
    returns:
        Prophet: the forecast model
    """
    def get_model(self)-> Prophet:
        return self._forecaster_model