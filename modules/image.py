from PyQt6.QtWidgets import QLabel
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt6.QtGui import QPixmap, QImage
import os 
class ImageApp(QLabel):
    def __init__(self, parent, name, width, height):
        QLabel.__init__(self, parent)
        self.setFixedSize(width, height)
        self.path = os.path.abspath(os.path.join(__file__, "..", "..","images", name))
        self.image = Image.open(self.path)
        self.imageQt = ImageQt(self.image)
        self.pixmap1 = QPixmap(QImage(self.imageQt)).scaled(width, height)
        self.setPixmap(self.pixmap1)
