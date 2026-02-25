from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class ForecastTemplate(QFrame):
    def __init__(self, text):
        super().__init__()

        self.setObjectName("ForecastTemplate")

        self.layout1 = QVBoxLayout(self)
        self.layout1.setContentsMargins(16, 16, 16, 16)
        self.layout1.setSpacing(16)

        title_frame = QFrame()
        title_frame.setObjectName("ForecastTitleFrame")

        layout_frame = QVBoxLayout(title_frame)
        layout_frame.setSpacing(8)
        layout_frame.setContentsMargins(0, 0, 0, 0)

        title = QLabel(text)
        title.setObjectName("weatherTodayTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)

        line = QFrame()
        line.setObjectName("ForecastLine")
        line.setFixedHeight(1)

        layout_frame.addWidget(title)
        layout_frame.addWidget(line)

        self.layout1.addWidget(title_frame)
        self.layout1.addStretch()