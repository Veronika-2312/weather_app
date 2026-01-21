from PyQt6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QWidget,
    QHBoxLayout
)

from .window import window
from .sidebar import Sidebar
from .panels import Panels
from .panels.header import Header

class Content(QFrame):
    def __init__(self):
        super().__init__()

        self.vlayout = QVBoxLayout(self)
        self.vlayout.setContentsMargins(20, 20, 20, 20)
        self.vlayout.setSpacing(20)

        self.vlayout.addWidget(Header())
        self.vlayout.addWidget(Panels())
        self.vlayout.addStretch()


main_widget = QWidget()
main_widget.setStyleSheet("background-color: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 1, stop: 0 rgba(255, 223, 86, 1), stop: 1 rgba(135, 206, 250, 1) ) ;")

layout = QHBoxLayout(main_widget)
layout.setContentsMargins(0, 0, 0, 0)
layout.setSpacing(0)

sidebar = Sidebar()
content = Content()

layout.addWidget(sidebar)
layout.addWidget(content)

window.setCentralWidget(main_widget)