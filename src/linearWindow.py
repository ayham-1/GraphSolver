from PyQt5 import QtWidgets, uic
import matplotlib.pyplot as plt
import numpy as np


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
        m = float(self.mBox.text())
        c = float(self.cBox.text())
        x = np.linspace(-5, 5, 100)
        y = m * x + c
        plt.figure(num="Linear Graph")
        plt.plot(x, y, '-r', label='y=' + str(m) + 'x' + '+' + str(c))
        plt.axhline()
        plt.axvline()
        plt.title("Graph of y=" + str(m) + "x" + "+" + str(c))
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc="upper left")
        plt.grid()
        plt.show()
                                                                                                                                                                                                         
