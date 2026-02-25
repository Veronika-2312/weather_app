from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QScrollArea,
    QWidget
)
from PyQt6.QtCore import Qt
from .forecast_template import ForecastTemplate
from .weather_item import WeatherItem
from ..utils import get_weather


class WeatherToday(ForecastTemplate):
    def __init__(self):
        super().__init__("Погода сегодня")

        self.setObjectName("WeatherToday")
        self.setFixedHeight(157)

        scroll = QScrollArea()
        scroll.setObjectName("WeatherTodayScroll")
        scroll.setFixedHeight(82)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        scroll.viewport().setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        scroll.setStyleSheet("background: transparent;")

        container = QWidget()
        container.setObjectName("WeatherTodayContainer")
        container.setFixedHeight(82)
        container.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        container.setStyleSheet("background: transparent;")


        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        self.weather = get_weather("dnipro", True)
        self.list_weather = self.weather.get("list")
        self.list_items = []
        for weather in self.list_weather:
            temp = int(weather.get("main").get("temp"))
            time = weather.get("dt_txt")[11:13]
            icon = weather.get("weather")[0].get("icon")
            item = WeatherItem(temp, time, f"icons/dark/{icon}.svg")
            layout.addWidget(item)
            self.list_items.append(item)

        layout.addStretch()
        scroll.setWidget(container)

        self.layout1.addWidget(scroll)