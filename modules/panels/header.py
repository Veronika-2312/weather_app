from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QLabel
)
from PyQt6.QtCore import Qt
from ..image import ImageApp


class Header(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("Header")
        self.setFixedHeight(36)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(12)

        left_layout = QHBoxLayout()
        left_layout.setSpacing(6)

        self.settings_icon_frame = QFrame()
        self.settings_icon_frame.setObjectName("HeaderIconFrame")
        self.settings_icon_frame.setFixedSize(36, 36)

        self.icon_layout = QHBoxLayout(self.settings_icon_frame)
        self.icon_layout.setContentsMargins(0, 0, 0, 0)

        self.settings_icon = ImageApp(self.settings_icon_frame, "settings_dark.png", 16, 16)
        self.icon_layout.addWidget(self.settings_icon, alignment=Qt.AlignmentFlag.AlignCenter)

        settings_text = QLabel("Настройки")
        settings_text.setObjectName("HeaderText")

        left_layout.addWidget(self.settings_icon_frame)
        left_layout.addWidget(settings_text)

        main_layout.addLayout(left_layout)

        main_layout.addStretch()

        right_layout = QHBoxLayout()
        right_layout.setSpacing(6)

        search_icon = ImageApp(self, "search.png", 22, 22)

        search_text = QLabel("Поиск")
        search_text.setObjectName("HeaderText")

        right_layout.addWidget(search_icon)
        right_layout.addWidget(search_text)

        main_layout.addLayout(right_layout)