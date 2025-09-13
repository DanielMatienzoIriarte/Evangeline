from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib as mpl

# Use the Agg backend for consistency when integrating with Qt
mpl.use('QtAgg')


class ProphetPlotCanvas(FigureCanvas):
    """A custom Matplotlib canvas widget for use in PyQt6."""

    def __init__(self, parent=None):
        fig = Figure()
        super().__init__(fig)
        self.setParent(parent)

    def update_plot_from_figure(self, figure):
        """
        Updates the canvas with a new Matplotlib Figure object.
        """
        self.figure = figure
        # Clear the old figure and copy content from the new figure
        self.figure.clear()
        self.figure.canvas = self  # Reconnect canvas to figure
        figure.axes[0].figure = self.figure  # Reconnect axes to figure

        # Copy the content of the new figure into the canvas figure
        # This requires manually copying content or using a deepcopy,
        # but a simpler approach is to use Prophet's plotting directly.
        # Alternatively, clear and redraw axes, but Prophet's `plot`
        # method makes a new Figure anyway. The simplest is to just
        # replace the Figure instance entirely.

        print(f"dsdsdsdsd:")
        self._figure = figure
        self.draw_idle()


class ProphetView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Prophet Forecast with PyQt6 MVC")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create the Matplotlib canvas widget and add it to the layout
        self.plot_canvas = ProphetPlotCanvas()
        layout.addWidget(self.plot_canvas)

    def show_plot(self, figure):
        """
        Called by the controller to update the plot.
        """
        self.plot_canvas.update_plot_from_figure(figure)