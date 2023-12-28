import sys
from PySide6.QtCore import *
from PySide6.QtGui import QMouseEvent, QPixmap, QPainter, QFont
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
import random

class fish:
    def __init__(self):
        self.image = QPixmap("images/fish.png")
        self.x = 0
        self.y = 0
        self.w = 40
        self.h = 40

    def draw(self, p):
        p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.image)

    def random_pos(self, arena_w, arena_h):
        self.x = random.randint(0, arena_w - self.w)
        self.y = random.randint(0, arena_h - self.h)

    def is_hit(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.w and self.y <= mouse_y <= self.y + self.h

class Animation_area(QWidget):
    def __init__(self, num_fishs=10):
        QWidget.__init__(self, None)
        self.setMinimumSize(300, 300)
        self.arena_w = 300
        self.arena_h = 300
        self.fishs = [fish() for _ in range(num_fishs)]
        self.remaining_fishs = num_fishs
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_value)
        self.timer.start(800)
        self.QSH = QSoundEffect()
        self.QSH.setSource(QUrl.fromLocalFile("sounds/fish_hit.wav"))
        self.QSM = QSoundEffect()
        self.QSM.setSource(QUrl.fromLocalFile("sounds/fish_missed.wav"))
        self.score = 0
        self.end_game = False
        self.background_image = QImage("images/underwater.png")

    def mousePressEvent(self, e):
        if self.end_game:
            return

        mouse_x = e.pos().x()
        mouse_y = e.pos().y()

        for fish in self.fishs:
            if fish.is_hit(mouse_x, mouse_y):
                self.QSH.play()
                print("Hit")
                self.fishs.remove(fish)
                self.remaining_fishs -= 1
                self.score += 1
                break
        else:
            self.QSM.play()
            print("Miss")

        if self.remaining_fishs == 0:
            self.end_game = True
            self.update()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        # Draw background image
        p.drawImage(self.rect(), self.background_image)

        for fish in self.fishs:
            fish.draw(p)

        # Display score on the top right
        p.setPen(Qt.white)
        font = QFont()
        font.setPointSize(18)
        p.setFont(font)
        p.drawText(self.width() - 80, 30, f"Score: {self.score}")

        if self.end_game:
            self.show_end_game(p)

        p.end()


    def update_value(self):
        if not self.end_game:
            for fish in self.fishs:
                fish.random_pos(self.arena_w, self.arena_h)
            self.update()

    def show_end_game(self, p):
        p.setPen(Qt.white)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        p.setFont(font)
        p.drawText(self.width() / 3, self.height() / 2, "End Game!")

class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.anim_area = Animation_area(num_fishs=10)
        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)
        self.setLayout(layout)
        self.setMinimumSize(330, 400)

def main():
    app = QApplication(sys.argv)
    w = Simple_animation_window()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
