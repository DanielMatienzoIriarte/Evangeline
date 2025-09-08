import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt6.QtCore import QObject, pyqtSignal

# Model
class DataModel(QObject):
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

# View
class DataView(QWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.label = QLabel("Current Data: ")
        self.input_field = QLineEdit()
        self.update_button = QPushButton("Update Data")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.update_button)
        self.setLayout(self.layout)

    def set_data_display(self, data: str):
        self.label.setText(f"Current Data: {data}")

    def get_input_data(self) -> str:
        return self.input_field.text()

# Controller
class DataController(QObject):
    def __init__(self, model: DataModel, view: DataView):
        super().__init__()
        self._model: DataModel = model
        self._view: DataView = view

        # Connect view signals to controller slots
        self._view.update_button.clicked.connect(self.update_model_from_view)

        # Connect model signals to view slots
        self._model.data_changed.connect(self._view.set_data_display)

        # Initialize view with current model data
        self._view.set_data_display(self._model.data)

    def update_model_from_view(self):
        new_data: str = self._view.get_input_data()
        self._model.data = new_data

# Main Application
class App(QApplication):
    def __init__(self, argv: list[str]):
        super().__init__(argv)
        self.model = DataModel("Initial Value")
        self.view = DataView()
        self.controller = DataController(self.model, self.view)
        self.view.setWindowTitle("PyQt6 MVC Example")
        self.view.show()

if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec())