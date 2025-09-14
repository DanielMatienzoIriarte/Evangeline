from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class F1PredictionView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("F1")
        self.setStyleSheet("background-color: gray;color:black;")
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel("Current Data: ")
        self.input_field = QLineEdit()
        self.update_button = QPushButton("Update Data")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.update_button)
        self.setLayout(self.layout)