from PyQt6.QtCore import QObject

from f1_prediction.f1_prediction_model import F1PredictionModel
from f1_prediction.f1_prediction_view import  F1PredictionView


class F1PredictionController(QObject):
    def __init__(self, model: F1PredictionModel, view: F1PredictionView):
        super().__init__()