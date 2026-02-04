from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtSvgWidgets import QSvgWidget
import os

class WeatherItem(QFrame):
    def __init__(self, temp:int , time: int, image_name: str):
        super().__init__()

        self.setFixedSize(45, 82)
        self.setObjectName("WeatherItem")

        layout = QVBoxLayout(self)
        layout.setSpacing(6)
        layout.setContentsMargins(0, 6, 0, 6)

        self.time_label = QLabel(time)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.path = os.path.abspath(os.path.join(__file__, "..", "..", "..", "images", image_name))
        self.icon= QSvgWidget(self.path)
        self.icon.setFixedSize(24, 24)

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.temp_label = QLabel(str(temp)+"°")
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.time_label)
        layout.addWidget(self.icon)
        layout.addWidget(self.temp_label)