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

        main = QVBoxLayout(self)
        main.setContentsMargins(16, 16, 16, 16)
        main.setSpacing(16)


        today = QLabel("Сегодня")
        today.setObjectName("Today")
        today.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main.addWidget(today)


        line = QFrame()
        line.setFixedSize(358, 1)
        main.addWidget(line)
        line.setObjectName("Line")

        row = QHBoxLayout()

        self.day_label = QLabel()
        self.day_label.setObjectName("Day")

        self.date_label = QLabel()
        self.date_label.setObjectName("Date")

        row.addWidget(self.day_label)
        row.addStretch()
        row.addWidget(self.date_label)
        main.addLayout(row)

        main.addStretch()


        clock_box = QWidget(self)
        clock_box.setFixedSize(170, 170)
        self.clock = ImageApp(clock_box, "clock.png", 170, 170)
        self.clock.setObjectName("Clock")
        self.clock.setGeometry(0, 0, 170, 170)

        self.time_label = QLabel(clock_box)
        self.time_label.setObjectName("Time")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setGeometry(0, 0, 170, 170)
        self.time_label.raise_()

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