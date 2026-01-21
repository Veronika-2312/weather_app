from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QLabel, QWidget
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import os
from ..image import ImageApp


class Header(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("Header")
        self.setFixedHeight(36)
        self.setStyleSheet("background-color: transparent")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)

        left = QHBoxLayout()
        left.setSpacing(6)

        settings_icon_frame = QFrame()
        settings_icon_frame.setFixedSize(36, 36)
        settings_layout = QHBoxLayout()
        settings_icon_frame.setLayout(settings_layout)
        settings_icon = ImageApp(settings_icon_frame, "settings.png", 16, 16)
        settings_layout.addWidget(settings_icon)
        settings_layout.setContentsMargins(0, 0, 0, 0)

        settings_icon_frame.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 4px")
        settings_icon.setStyleSheet("background-color: transparent")

        settings_text = QLabel("Настройки")
        settings_text.setObjectName("settings_text")

        left.addWidget(settings_icon_frame)
        left.addWidget(settings_text)

        layout.addLayout(left)

   
        layout.addStretch()

 
        right = QHBoxLayout()
        right.setSpacing(6)

        search_icon = ImageApp(self, "search.png", 22, 22)
        search_text = QLabel("Поиск")
        search_text.setObjectName("search_text")

        right.addWidget(search_icon)
        right.addWidget(search_text)

        layout.addLayout(right)