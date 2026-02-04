from PyQt6.QtWidgets import QWidget, QVBoxLayout
from .weather_today import WeatherToday
from .forecast_12h import Forecast12H


class LowerPanels(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)

        layout.addWidget(WeatherToday())
        layout.addWidget(Forecast12H())