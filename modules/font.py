from PyQt6.QtGui import QFont, QFontDatabase
import os 
from .app import app

path = os.path.abspath(__file__ + "/../../Roboto.ttf")
print(path)
font_id = QFontDatabase.addApplicationFont(path)
print(font_id)
font = QFontDatabase.applicationFontFamilies(font_id)[0]
app.setFont(QFont(font))