from PyQt6.QtWidgets import QMainWindow

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(100,100,1200,800)
        self.setWindowTitle("app")
        
window = Window()