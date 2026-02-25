from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt
from .forecast_template import ForecastTemplate
from ..utils.get_graphic import get_graphic


class Forecast12H(ForecastTemplate):
    def __init__(self):
        super().__init__("Прогноз на 12 часов")

        self.setObjectName("Forecast12H")
        self.setFixedHeight(197)

        main_frame = QFrame()
        main_frame.setObjectName("ForecastMainFrame")

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(10)
        main_frame.setLayout(main_layout)
        main_frame.setFixedSize(755, 106)

        graphic_frame = QFrame()
        graphic_frame.setObjectName("GraphicFrame")

        graphic_layout = QHBoxLayout()
        graphic_layout.setContentsMargins(0, 0, 0, 0)
        graphic_layout.setSpacing(4)
        graphic_frame.setLayout(graphic_layout)
        graphic_frame.setFixedSize(700, 106)

        list_temp, list_height = get_graphic(city_name="dnipro")

        for height in list_height:
            temp_frame = QFrame()
            temp_frame.setObjectName("GraphBar")
            temp_frame.setFixedWidth(8)
            temp_frame.setFixedHeight(int(height))

            graphic_layout.addWidget(
                temp_frame,
                alignment=Qt.AlignmentFlag.AlignBottom
            )

        axis_frame = QFrame()
        axis_frame.setObjectName("GraphAxisFrame")

        axis_layout = QVBoxLayout()
        axis_layout.setContentsMargins(0, 0, 0, 0)
        axis_layout.setSpacing(0)
        axis_frame.setLayout(axis_layout)
        axis_frame.setFixedWidth(45)

        axis_values = list(range(15, -20, -5))

        for value in axis_values:
            label = QLabel(str(value))
            label.setObjectName("GraphAxis")
            label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            axis_layout.addWidget(label)

        main_layout.addWidget(graphic_frame)
        main_layout.addWidget(axis_frame)

        self.layout1.addWidget(main_frame)