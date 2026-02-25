from PyQt6.QtWidgets import QMainWindow
import os
from .app import app
from .content import main_widget, content, sidebar
from .image  import ImageApp
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1200, 800)
        self.setWindowTitle("Weather App")

        
        self.thema = "dark"
        self.main_widget = None

    def apply_theme(self):
        self.thema = "dark" if self.thema == "light" else "light"
        if not self.main_widget:
            return
        if self.thema == "dark":
            list_files = ["main.qss", "dark.qss"]
        else:
            list_files = ["main.qss", "light.qss"]
        
        content.header.settings_icon.deleteLater()
        content.header.settings_icon = ImageApp(content.header.settings_icon_frame, f"settings_{self.thema}.png", 16, 16)
        content.header.icon_layout.addWidget(content.header.settings_icon, alignment=Qt.AlignmentFlag.AlignCenter)
        for item in content.lower_panels.weather_today.list_items:
            item.change_thema(self.thema)

        for name in list_files:
            path = os.path.abspath(os.path.join(__file__, "..", "..","styles", name))
            with open(path) as file: 
                app.setStyleSheet(app.styleSheet() + file.read())
        

window = Window()

window.main_widget = main_widget
window.setCentralWidget(main_widget)
window.apply_theme()
sidebar.theme_btn.clicked.connect(window.apply_theme)
