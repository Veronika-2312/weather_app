from PyQt6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QWidget,
    QHBoxLayout
)

from .sidebar import Sidebar
from .panels.header import Header
from .panels import Panels, LowerPanels


class Content(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        self.header = Header()
        layout.addWidget(self.header)
        self.panels = Panels()
        layout.addWidget(self.panels)
        self.lower_panels = LowerPanels()
        layout.addWidget(self.lower_panels)
        layout.addStretch()



main_widget = QWidget()


main_widget.setObjectName("MainWidget")

layout = QHBoxLayout(main_widget)
layout.setContentsMargins(0, 0, 0, 0)
layout.setSpacing(0)
sidebar = Sidebar()
layout.addWidget(sidebar)
content = Content()
layout.addWidget(content)

