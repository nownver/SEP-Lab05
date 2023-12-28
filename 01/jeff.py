import sys
from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
from PySide6.QtGui import *

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/jeff1.jpg")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon(
            [QPoint( 0, 100), QPoint(100, 100),
            QPoint (0, 0), QPoint (100, 0), ])
        p.drawPixmap(QRect (200, 100, 320, 320), self.rabbit)
        p.end()
