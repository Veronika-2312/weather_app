from PyQt6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QPushButton,
    QScrollArea,
    QWidget
)
from PyQt6.QtCore import Qt
from datetime import timezone, timedelta, datetime

from .city import City
from .utils import get_weather


city_list = ["Днепр", "Киев", "Братислава", "Варшава", "Рим"]


class Sidebar(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("Sidebar")

        self.setFixedWidth(370)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        self.theme_btn = QPushButton("☾")
        self.theme_btn.setFixedSize(26, 26)
        self.theme_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.theme_btn.setObjectName("ThemeBtn")

        main_layout.addWidget(self.theme_btn, alignment=Qt.AlignmentFlag.AlignRight)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll.setObjectName("SidebarScrollArea")

        main_layout.addWidget(scroll, 1)

        scroll_content = QWidget()
        scroll_content.setObjectName("SidebarScroll")
        scroll.setWidget(scroll_content)

        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(10)


        for city in city_list:
            weather = get_weather(city)
            time_zone = timedelta(seconds=weather["timezone"])
            time = (datetime.now(timezone.utc) + time_zone).strftime("%H:%M")

            scroll_layout.addWidget(
                City(
                    city,
                    time,
                    weather["weather"][0]["description"],
                    f"{round(weather['main']['temp'])}°",
                    f"Макс:{round(weather['main']['temp_max'])}°  Мин:{round(weather['main']['temp_min'])}°",
                    active=city == "Днепр"
                )
            )

        scroll_layout.addStretch()

