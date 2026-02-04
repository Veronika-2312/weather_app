from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class ForecastTemplate(QFrame):
    def __init__(self, text):
        super().__init__()

        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 10px;")

        self.layout1 = QVBoxLayout(self)
        self.layout1.setContentsMargins(16, 16, 16, 16)
        self.layout1.setSpacing(16)

        title_frame = QFrame()
        layout_frame = QVBoxLayout(title_frame)
        layout_frame.setSpacing(8)
        layout_frame.setContentsMargins(0, 0, 0, 0)
        title_frame.setStyleSheet("background-color: transparent")
        title = QLabel(text)
        title.setObjectName("weatherTodayTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("background-color: transparent; color: white;")
        
        line = QFrame()
        line.setStyleSheet("background-color: rgba(255, 255, 255, 0.2)")
        line.setFixedHeight(1)

        layout_frame.addWidget(title)
        layout_frame.addWidget(line)
        self.layout1.addWidget(title_frame)
        self.layout1.addStretch()