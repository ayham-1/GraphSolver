from PyQt5 import QtWidgets, uic
import matplotlib.pyplot as plt
import numpy as np

class linearInterceptWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(linearInterceptWin, self).__init__()
        self.ui = uic.loadUi("ui/linearInterceptWindow.ui", self)

        # Get calcBtn, and connect it to stuff.
        self.calcBtn = self.findChild(QtWidgets.QPushButton, "calcBtn")
        self.calcBtn.clicked.connect(self.calcBtnPressed)

        # Get line1mBox
        self.line1mBox = self.findChild(QtWidgets.QLineEdit, "line1mBox")
        # Get line1cBox
        self.line1cBox = self.findChild(QtWidgets.QLineEdit, "line1cBox")

        # Get line2mBox
        self.line2mBox = self.findChild(QtWidgets.QLineEdit, "line2mBox")
        # Get line2cBox
        self.line2cBox = self.findChild(QtWidgets.QLineEdit, "line2cBox")

        # Get resultXBox
        self.resultXBox = self.findChild(QtWidgets.QLineEdit, "resultXBox")
        # Get resultYBox
        self.resultYBox = self.findChild(QtWidgets.QLineEdit, "resultYBox")

        self.ui.show()

    def calcBtnPressed(self):

        m1 = float(self.line1mBox.text())
        c1 = float(self.line1cBox.text())
        m2 = float(self.line2mBox.text())
        c2 = float(self.line2cBox.text())
        x = np.linspace(-5,5,100)
        xm = (c2 - c1) / (m1 - m2)
        y1 = m1 * x + c1
        y2 = m2 * x + c2
        ym = m1 * xm + c1
        self.resultXBox.setText(str(xm))
        self.resultYBox.setText(str(ym))
        plt.figure(num="Linear Intercept")
        plt.plot(x, y1, '-r')
        plt.plot(x, y2, 'limegreen')
        plt.scatter(xm,ym, color="black")
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.axhline()
        plt.axvline()
        plt.grid()
        plt.show()
