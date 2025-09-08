from PyQt6.QtWidgets import QWidget, QMainWindow
from PyQt6.QtCore import Qt, QObject

from new_delhi_weather.new_delhi_weather_model import NewDelhiWeather as Model
from new_delhi_weather.new_delhi_weather_controller import NewDelhiWeather as Controller
from new_delhi_weather.new_delhi_weather_view import NewDelhiWeather as View


class NewDelhiWeather(QObject):
    def __init__(self, parent: QMainWindow):
        super().__init__()

        self._model = Model()
        self._view = View()
        self._controller = Controller(self._model, self._view)

    def display_ui(self):
        self._view.show()