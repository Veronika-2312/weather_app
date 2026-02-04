from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from .forecast_template import ForecastTemplate


class Forecast12H(ForecastTemplate):
    def __init__(self):
        super().__init__("Прогноз на 12 часов")

        self.setObjectName("Forecast12H")
        self.setFixedHeight(197)
     