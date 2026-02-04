from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class WeatherPanel(QFrame):
    def __init__(self, weather):
        super().__init__()

        self.weather = weather
        self.setFixedSize(390, 303)
        self.setObjectName("WeatherPanel")
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.2)")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)

        position = QLabel("текущая позиция")
        position.setStyleSheet("background-color: transparent")
        position.setObjectName("position")
        position.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(position)

        line = QFrame()
        line.setFixedSize(358,1)
        layout.addWidget(line)
        line.setStyleSheet("background-color: rgba(255, 255, 255, 0.2)")

        layout.addStretch()

        city = QLabel("Днепр")
        city.setObjectName("city")
        city.setAlignment(Qt.AlignmentFlag.AlignCenter)
        city.setStyleSheet("background-color: transparent")

        temp_value = round(self.weather["main"]["temp"])
        self.temp_label = QLabel(f"{temp_value}°")
        self.temp_label.setObjectName("temp_label")
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp_label.setStyleSheet("background-color: transparent")

        desc = self.weather["weather"][0]["description"]
        self.desc_label = QLabel(desc.capitalize())
        self.desc_label.setObjectName("desc_label")
        self.desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.desc_label.setStyleSheet("background-color: transparent")

        min_t = round(self.weather["main"]["temp_min"])
        max_t = round(self.weather["main"]["temp_max"])
        self.minmax_label = QLabel(f"Макс: {max_t}°  Мин: {min_t}°")
        self.minmax_label.setObjectName("minmax_label")
        self.minmax_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.minmax_label.setStyleSheet("background-color: transparent")

        layout.addWidget(city)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.desc_label)
        layout.addWidget(self.minmax_label)
        layout.addStretch()