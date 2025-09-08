from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from prophet.plot import plot_plotly
from plotly.graph_objs import Figure

from new_delhi_weather_mvvm.new_delhi_weather_viewmodel import NewDelhiWeather as viewModel
from new_delhi_weather_mvvm.new_delhi_weather_model import NewDelhiWeather as model


class NewDelhiWeather(QWidget):

    def __init__(self):
        
        super().__init__()

        self._model = model()
        self._viewmodel = viewModel(self._model)

        self.layout = None
        self.label = None
        self.button = None
        self.figure = None

        self.init_ui()
        self.bind_view_model()

    """
    Initializes the UI and renders a window displaying weather forecast.
    """
    def init_ui(self):
        self.setWindowTitle('Weather Prediction')
        #self.showMaximized()
        self.layout = QVBoxLayout()
        self.label = QLabel('0')
        self.layout.addWidget(self.label)
        self.button = QPushButton('Predict')
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    """
    Connect UI elements to the ViewModel
    """
    def bind_view_model(self):
        self.button.clicked.connect(self._viewmodel.generate_prediction)
        self._viewmodel.graphic_updated.connect(self.update_frame)
        self.figure = plot_plotly(self._viewmodel.generate_prediction, predictions)

        self.update_frame(self.figure)

    """
    Updates the view to redender the forecasted graph.

    params:
    figure: Figure 
    """
    def update_frame(self, figure: Figure):
        figure.show()