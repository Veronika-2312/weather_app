from PyQt6.QtWidgets import QApplication
import os

app = QApplication([]) 
list_files = ["weather.qss", "time.qss", "header.qss"]
for name in list_files:
    path = os.path.abspath(os.path.join(__file__, "..", "..","styles", name))
    with open(path) as file: 
        app.setStyleSheet(app.styleSheet() + file.read())
