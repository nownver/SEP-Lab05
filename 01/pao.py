import sys
from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
from PySide6.QtGui import *

class Bird(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit_frames = [QPixmap(f"images/tile{i}.png") for i in range(9)]
        self.current_frame = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(100)

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon(
            [QPoint( 20, 50), QPoint(50, 60),
            QPoint (80, 50), QPoint (50, 100), ])
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)
        p.drawPolygon( [QPoint (0, 150), QPoint(100, 150),
            QPoint (30, 250),] )
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit_frames[self.current_frame])
        p.end()

    def update_frame(self):
        self.current_frame += 1
        if self.current_frame >= len(self.rabbit_frames):
            self.current_frame = 0
        self.update()
