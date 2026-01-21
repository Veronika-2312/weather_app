from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt

class City(QFrame):  
    def __init__(self, city, time, desc, temp, minmax, active=False):
        QFrame.__init__(self)
        if active:
            self.setStyleSheet("""
                background-color: rgba(0, 0, 0, 0.2);
                border-radius: 8px;
            """)
        else:    
            self.setStyleSheet("""
                background-color: transparent;
                border-radius: 8px;
            """)
        self.setFixedHeight(90)
        row_layout = QHBoxLayout(self)
        row_layout.setContentsMargins(8, 8, 8, 8)

        left = QVBoxLayout()
        city_lbl = QLabel(city)
        city_lbl.setStyleSheet("color:white; font-size:22px; font-weight:500; background-color: transparent")


        time_lbl = QLabel(time)
        time_lbl.setStyleSheet("color:white; font-size:12px; opacity:0.8; background-color: transparent")

        desc_lbl = QLabel(desc)
        desc_lbl.setStyleSheet("color:white; font-size:12px; opacity:0.8; background-color: transparent")

        left.addWidget(city_lbl)
        left.addWidget(time_lbl)
        left.addWidget(desc_lbl)

        right = QVBoxLayout()
        temp_lbl = QLabel(temp)
        temp_lbl.setStyleSheet("color:white; font-size:44px; font-weight:500; opacity:0.8; background-color: transparent")

        minmax_lbl = QLabel(minmax)
        minmax_lbl.setStyleSheet("color:white; font-size:12px; opacity:0.8; background-color: transparent")

        right.addWidget(temp_lbl, alignment=Qt.AlignmentFlag.AlignRight)
        right.addWidget(minmax_lbl, alignment=Qt.AlignmentFlag.AlignRight)

        row_layout.addLayout(left)
        row_layout.addStretch()
        row_layout.addLayout(right)
