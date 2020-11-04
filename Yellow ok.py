import random, sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import QPoint
from PyQt5 import uic


class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.qp = QPainter()
        self.show()

        self.flag = False

        self.ok.clicked.connect(self.begin)

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def begin(self):
        self.flag = True
        self.repaint()

    def draw(self):
        self.qp.setBrush(QColor('#ffff00'))
        a = random.randint(0, 100)
        self.qp.drawEllipse((QPoint(self.width() // 2, self.height() // 2)), a, a)


if __name__ == '__main__':
    ex = QApplication(sys.argv)
    am = FirstWindow()
    sys.exit(ex.exec())
