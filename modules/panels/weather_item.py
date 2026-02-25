from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtSvgWidgets import QSvgWidget
import os

class WeatherItem(QFrame):
    def __init__(self, temp:int , time: int, image_name: str):
        super().__init__()

        self.setFixedSize(45, 82)
        self.setObjectName("WeatherItem")

        self.layout_v = QVBoxLayout(self)
        self.layout_v.setSpacing(6)
        self.layout_v.setContentsMargins(0, 6, 0, 6)
        
        self.time_label = QLabel(time)
        self.time_label.setObjectName("Timelabel")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.path = os.path.abspath(os.path.join(__file__, "..", "..", "..", "images", image_name))
        self.icon= QSvgWidget(self.path)
        self.icon.setFixedSize(24, 24)

        self.layout_v.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.temp_label = QLabel(str(temp)+"°")
        self.temp_label.setObjectName("Templabel")
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_v.addWidget(self.time_label)
        self.layout_v.addWidget(self.icon)
        self.layout_v.addWidget(self.temp_label)
    def change_thema(self,thema):
        self.icon.deleteLater()
        if thema == "dark":
            self.path = self.path.replace("light","dark")
        else:
            self.path = self.path.replace("dark","light")

        self.icon= QSvgWidget(self.path)
        self.icon.setFixedSize(24, 24)
        self.layout_v.insertWidget(1, self.icon)
        

        
