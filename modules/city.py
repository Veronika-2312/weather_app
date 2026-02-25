from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt


class City(QFrame):
    def __init__(self, city, time, desc, temp, minmax, active=False):
        super().__init__()

        if active:
            self.setObjectName("ActiveCity")
        else:
            self.setObjectName("CityItem")

        self.setFixedHeight(90)

        row_layout = QHBoxLayout(self)
        row_layout.setContentsMargins(8, 8, 8, 8)

        left = QVBoxLayout()
        city_lbl = QLabel(city)
        city_lbl.setObjectName("CityName")

        time_lbl = QLabel(time)
        time_lbl.setObjectName("CityTime")

        desc_lbl = QLabel(desc)
        desc_lbl.setObjectName("CityDesc")

        left.addWidget(city_lbl)
        left.addWidget(time_lbl)
        left.addWidget(desc_lbl)

        right = QVBoxLayout()
        temp_lbl = QLabel(temp)
        temp_lbl.setObjectName("CityTemp")

        minmax_lbl = QLabel(minmax)
        minmax_lbl.setObjectName("CityMinmax")


        right.addWidget(temp_lbl, alignment=Qt.AlignmentFlag.AlignRight)
        right.addWidget(minmax_lbl, alignment=Qt.AlignmentFlag.AlignRight)

        row_layout.addLayout(left)
        row_layout.addStretch()
        row_layout.addLayout(right)
