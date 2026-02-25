from PyQt6.QtWidgets import QWidget, QVBoxLayout
from .weather_today import WeatherToday
from .forecast_12h import Forecast12H


class LowerPanels(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        self.weather_today = WeatherToday()
        layout.addWidget(self.weather_today)
        self.forecast_12h = Forecast12H()
        layout.addWidget(self.forecast_12h)