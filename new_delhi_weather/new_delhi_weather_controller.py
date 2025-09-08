
import sys
from PyQt6.QtCore import QObject

from new_delhi_weather.new_delhi_weather_model import NewDelhiWeather as Model
from new_delhi_weather.new_delhi_weather_view import NewDelhiWeather as View


class NewDelhiWeather(QObject):
    def __init__(self, model: Model, view: View):
        super().__init__()
        self._model: Model = model
        self._view: View = view

        # Connect view signals to controller slots
        self._view.update_button.clicked.connect(self.update_model_from_view)

        # Connect model signals to view slots
        self._model.data_changed.connect(self._view.set_data_display)

        # Initialize view with current model data
        self._view.set_data_display(self._model.data)

    def update_model_from_view(self):
        new_data: str = self._view.get_input_data()
        self._model.data = new_data