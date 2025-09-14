from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar, FigureCanvasQTAgg as MplCanvas
from plotly.graph_objs import Figure

from new_delhi_weather.new_delhi_weather_canvas import NewDelhiWeatherCanvas


class NewDelhiWeather(QWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self._canvas = None

        self.setWindowTitle("Weather222")
        self.setStyleSheet("background-color: gray;color:black;")
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel("Current Data: ")
        self.input_field = QLineEdit()
        self.update_button = QPushButton("Update Weather Data")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.update_button)
        self.setLayout(self.layout)

    def set_data_display(self, data: str):
        self.label.setText(f"Current Data: {data}")

    def get_input_data(self) -> str:
        return self.input_field.text()

    def set_weather_data(self, figure: Figure):
        # research update with new data
        """if self._canvas:
            self.layout.removeWidget(self._canvas)
            # self._canvas.delete()
            self._canvas = None"""

        self._canvas = NewDelhiWeatherCanvas(self, figure)
        toolbar = NavigationToolbar(self._canvas, self)
        self.layout.addWidget(toolbar)
        self.layout.addWidget(self._canvas)

        """self.canvas.update_plot_from_figure(figure)
        self.canvas.draw()"""