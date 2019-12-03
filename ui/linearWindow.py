from PyQt5 import QtWidgets, uic
from methods.linear.calcLinear import Linear
import matplotlib.pyplot as plt


class linearWin(QtWidgets.QMainWindow):
    m = 0.0
    c = 0.0

    def __init__(self):
        super(linearWin, self).__init__()
        self.ui = uic.loadUi("ui/linearWindow.ui", self)

        # Get calcBtn, and connect it to stuff.
        self.calcBtn = self.findChild(QtWidgets.QPushButton, "calcBtn")
        self.calcBtn.clicked.connect(self.calcBtnPressed)

        # Get mBox, and connect it to stuff.
        self.mBox = self.findChild(QtWidgets.QLineEdit, "mBox")
        # Get cBox, and connect it to stuff.
        self.cBox = self.findChild(QtWidgets.QLineEdit, "cBox")

        self.ui.show()

    def calcBtnPressed(self):
        m = int(self.mBox.text())
        c = int(self.cBox.text())
        linear = Linear(m, c, 2)
        plt.plot(linear.calc_linear_line())
        plt.ylabel("Y")
        plt.xlabel("X")
        plt.show()
