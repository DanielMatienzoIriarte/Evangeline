from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt6.QtWidgets import QSizePolicy

# Use the Agg backend for consistency when integrating with Qt
import matplotlib
matplotlib.use('QtAgg')


class NewDelhiWeatherCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, figure=Figure, width=5, height=4, dpi=100):
        #self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.figure = figure
        # self.axes = self.figure.add_subplot(111)
        super().__init__(self.figure)

        self.setParent(parent)
        #self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.updateGeometry()

    def update_plot_from_figure(self, figure: Figure) -> None:
        self.figure = figure
        self.figure.clear() # Clear the old figure and copy content from the new figure
        self.figure.canvas.figure = self.figure # Reconnect canvas to figure
        # self.figure.axes[0].set_figure = self.figure

        self.draw_idle()