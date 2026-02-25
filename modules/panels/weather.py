from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class WeatherPanel(QFrame):
    def __init__(self, weather):
        super().__init__()

        self.weather = weather
        self.setFixedSize(390, 303)
        self.setObjectName("WeatherPanel")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)

        position = QLabel("текущая позиция")
        position.setObjectName("position")
        position.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(position)

        line = QFrame()
        line.setObjectName("WeatherLine")
        line.setFixedSize(358, 1)
        layout.addWidget(line)

        layout.addStretch()

        city = QLabel("Днепр")
        city.setObjectName("city")
        city.setAlignment(Qt.AlignmentFlag.AlignCenter)

        temp_value = round(self.weather["main"]["temp"])
        self.temp_label = QLabel(f"{temp_value}°")
        self.temp_label.setObjectName("temp_label")
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        desc = self.weather["weather"][0]["description"]
        self.desc_label = QLabel(desc.capitalize())
        self.desc_label.setObjectName("desc_label")
        self.desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        min_t = round(self.weather["main"]["temp_min"])
        max_t = round(self.weather["main"]["temp_max"])
        self.minmax_label = QLabel(f"Макс: {max_t}°  Мин: {min_t}°")
        self.minmax_label.setObjectName("minmax_label")
        self.minmax_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(city)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.desc_label)
        layout.addWidget(self.minmax_label)
        layout.addStretch()