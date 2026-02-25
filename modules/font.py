from PyQt6.QtGui import QFont, QFontDatabase
import os 
from .app import app

path = os.path.abspath(__file__ + "/../../Roboto.ttf")
font_id = QFontDatabase.addApplicationFont(path)
font = QFontDatabase.applicationFontFamilies(font_id)[0]
app.setFont(QFont(font))