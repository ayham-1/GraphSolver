from PyQt5 import QtWidgets, uic
import matplotlib.pyplot as plt
import numpy as np


class quadraticWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(quadraticWin, self).__init__()
        self.ui = uic.loadUi("ui/quadraticWindow.ui", self)

        # Get calcBtn, and connect it to stuff.
        self.calcBtn = self.findChild(QtWidgets.QPushButton, "calcBtn")
        self.calcBtn.clicked.connect(self.calcBtnPressed)

        # Get aBox, and connect it to stuff.
        self.aBox = self.findChild(QtWidgets.QLineEdit, "aBox")
        # Get bBox, and connect it to stuff.
        self.bBox = self.findChild(QtWidgets.QLineEdit, "bBox")
        # Get cBox, and connect it to stuff.
        self.cBox = self.findChild(QtWidgets.QLineEdit, "cBox")

        self.ui.show()

    def calcBtnPressed(self):
        a = float(self.aBox.text())
        b = float(self.bBox.text())
        c = float(self.cBox.text())
        x = np.linspace(-10, 10, 100)
        y = a * x**2 + b * x + c
        graph = str(a) + 'x^2 + ' + str(b) + '*x + ' + str(c)
        plt.figure("Quadratic Graph")
        plt.axhline()
        plt.axvline()
        plt.plot(x, y, '-r', label=graph)
        plt.title("Graph of " + graph)
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc="upper left")
        plt.grid()
        plt.show()                   
