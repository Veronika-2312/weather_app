from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from .city import City
from .utils import get_weather
from datetime import timezone, timedelta, datetime

city_list = ["Днепр", "Киев", "Братислава",  "Варшава", "Рим"]
class Sidebar(QFrame):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(370)
        self.setStyleSheet("""
            background-color: rgba(0,0,0, 0.4);
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)
        
        for city in city_list:
            weather = get_weather(city)
            time_zone = timedelta(seconds=weather.get("timezone"))
            time = (datetime.now(timezone.utc)+ time_zone).strftime("%H:%M")
            layout.addWidget(City(
                city, time, weather.get("weather")[0].get("description"), f"{round(weather.get("main").get("temp"))}°", f"Макс:{round(weather.get("main").get("temp_max"))}°  Мин:{round(weather.get("main").get("temp_min"))}°", active=city == "Днепр"
            ))

        layout.addStretch()

