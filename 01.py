import sys
from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
from PySide6.QtGui import *
from jeff import Simple_drawing_window2
from yok import *

def main():
    app = QApplication(sys.argv)
    
    w = Simple_animation_window()
    w.show()
    
    w2 = Simple_drawing_window2()
    w2.show()
    
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())