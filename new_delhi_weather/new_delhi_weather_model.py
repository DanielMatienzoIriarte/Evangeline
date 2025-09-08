from PyQt6.QtCore import QObject, pyqtSignal
from plotly.graph_objs import Figure


class NewDelhiWeather(QObject):
    data_changed = pyqtSignal(str)

    def __init__(self, initial_data: str = ""):
        super().__init__()
        self._data: str = initial_data

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, value: str):
        if self._data != value:
            self._data = value
            self.data_changed.emit(self._data)