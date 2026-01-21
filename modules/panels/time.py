from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout,
    QLabel, QWidget
)
from PyQt6.QtCore import Qt
from datetime import datetime, timezone, timedelta
import os

from ..image import ImageApp


class TimePanel(QFrame):
    def __init__(self, weather):
        super().__init__()

        self.weather = weather
        self.setObjectName("TimePanel")
        self.setFixedSize(390, 303)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.2)")

        main = QVBoxLayout(self)
        main.setContentsMargins(16, 16, 16, 16)
        main.setSpacing(16)


        today = QLabel("Сегодня")
        today.setObjectName("today")
        today.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main.addWidget(today)
        today.setStyleSheet("background-color: transparent")


        line = QFrame()
        line.setFixedSize(358,1)
        main.addWidget(line)
        line.setStyleSheet("background-color: rgba(255, 255, 255, 0.2)")


        row = QHBoxLayout()

        self.day_label = QLabel()
        self.day_label.setObjectName("day")
        self.day_label.setStyleSheet("background-color: transparent")

        self.date_label = QLabel()
        self.date_label.setObjectName("date")
        self.date_label.setStyleSheet("background-color: transparent")

        row.addWidget(self.day_label)
        row.addStretch()
        row.addWidget(self.date_label)
        main.addLayout(row)

        main.addStretch()


        clock_box = QWidget(self)
        clock_box.setFixedSize(170, 170)
        clock_box.setStyleSheet("background-color: transparent")

        base_dir = os.path.dirname(__file__)
        img_path = os.path.join(base_dir, "..", "..", "images", "clock.png")

        self.clock = ImageApp(clock_box, img_path, 170, 170)
        self.clock.setGeometry(0, 0, 170, 170)
        self.clock.setStyleSheet("background-color: transparent")

        self.time_label = QLabel(clock_box)
        self.time_label.setObjectName("time")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setGeometry(0, 0, 170, 170)
        self.time_label.raise_()
        self.time_label.setStyleSheet("background-color: transparent")

        main.addWidget(clock_box, alignment=Qt.AlignmentFlag.AlignCenter)
        main.addStretch()

   
        tz = timedelta(seconds=self.weather["timezone"])
        now = datetime.now(timezone.utc) + tz

        self.time_label.setText(now.strftime("%H:%M"))
        self.date_label.setText(now.strftime("%d.%m.%Y"))

        days = [
            "Понедельник", "Вторник", "Среда",
            "Четверг", "Пятница", "Суббота", "Воскресенье"
        ]
        self.day_label.setText(days[now.weekday()])