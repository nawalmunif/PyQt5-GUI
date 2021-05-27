from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QPropertyAnimation, QPoint

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.child = QtWidgets.QLabel(self)
        self.child.setText("check")
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        self.anim = QPropertyAnimation(self.child, "pos")
        self.anim.setEndValue(QPoint(400, 400))
        self.anim.setDuration(1500)
        self.anim.start()
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = Window()
    w.show()


    sys.exit(app.exec_())