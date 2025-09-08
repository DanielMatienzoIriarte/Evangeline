import sys

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from prophet.plot import plot_plotly

from new_delhi_weather_mvvm.new_delhi_weather_model import NewDelhiWeather as model
from new_delhi_weather_mvvm.new_delhi_weather_viewmodel import NewDelhiWeather as viewModel
from new_delhi_weather_mvvm.new_delhi_weather_view import NewDelhiWeather as view


class NewDelhiWeather(QWidget):

    def __init__(self):
        
        super().__init__()

        self.model = model()
        self.view_model = viewModel(self.model)
        self.view = view()

        self.view.show()