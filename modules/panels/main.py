from PyQt6.QtWidgets import QWidget, QHBoxLayout
from .weather import WeatherPanel
from .time import TimePanel
from ..utils.get_weather import get_weather

class Panels(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(310)
        self.setStyleSheet("background-color: red")

        layout = QHBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(0, 0, 0, 0)

        weather = get_weather("Днепр")

        layout.addWidget(WeatherPanel(weather), 2)
        layout.addWidget(TimePanel(weather), 1)