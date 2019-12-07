from PyQt5 import QtWidgets, uic
import matplotlib.pyplot as plt
import numpy as np
import math



class cubicInterceptWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(cubicInterceptWin, self).__init__()
        self.ui = uic.loadUi("ui/cubicInterceptWindow.ui", self)

        # Get calcBtn, and connect it to stuff.
        self.calcBtn = self.findChild(QtWidgets.QPushButton, "calcBtn")
        self.calcBtn.clicked.connect(self.calcBtnPressed)

        # Get line1aBox
        self.line1aBox = self.findChild(QtWidgets.QLineEdit, "line1aBox")
        # Get line1bBox
        self.line1bBox = self.findChild(QtWidgets.QLineEdit, "line1bBox")
        # Get line1cBox
        self.line1cBox = self.findChild(QtWidgets.QLineEdit, "line1cBox")
        # Get line1dBox
        self.line1cBox = self.findChild(QtWidgets.QLineEdit, "line1cBox")

        # Get line2aBox
        self.line2aBox = self.findChild(QtWidgets.QLineEdit, "line2aBox")
        # Get line2bBox
        self.line2bBox = self.findChild(QtWidgets.QLineEdit, "line2bBox")
        # Get line2cBox
        self.line2cBox = self.findChild(QtWidgets.QLineEdit, "line2cBox")
        # Get line2dBox
        self.line2dBox = self.findChild(QtWidgets.QLineEdit, "line2dBox")

        # Get resultBox
        self.resultBox = self.findChild(QtWidgets.QTextEdit, "resultBox")

        self.ui.show()

    def calcBtnPressed(self):
        a1 = float(self.line1aBox.text())
        b1 = float(self.line1bBox.text())
        c1 = float(self.line1cBox.text())
        d1 = float(self.line1dBox.text())
        a2 = float(self.line2aBox.text())
        b2 = float(self.line2bBox.text())
        c2 = float(self.line2cBox.text())
        d2 = float(self.line2dBox.text())

        a = a2 - a1
        b = b2 - b1
        c = c2 - c1
        d = d2 - d1

        x = np.linspace(-10,10,100)
        yf = a1 * x**3 + b1 * x**2 + c1*x + d1
        ys = a2 * x**3 + b2 * x**2 + c2*x + d2
        ym = a * x**3 + b * x**2 + c * x + d

        if a == 0.0 and b == 0.0 and c == 0.0 and d == 0.0:
            self.resultBox.append(
                "These Two parabolas are the same \n All points interset.")
            return
        if a == 0.0:
            if b == 0.0:
                self.resultBox.append("These two parabolas do not intersect.")
                return
            else:
                x1 = -c / b
                y1 = a1 * x1 * x1 + b1 * x1 * x1 + c1 * x1 + d1
                self.resultBox.append("One Intersect: \n (x: " + str(x1) +
                                      ", y:" + str(y1))
                return
        discriminant = a**2 * b**2 + 18 * a * b * c - 4 * b**3 - 4 * a**3 * c - 27 * c**2

        if discriminant < 0.0:
            self.resultBox.append("These two parabolas do not intersect.")
            return
        elif discriminant == 0.0:
            x1 = -b / (2 * a)
            y1 = a1 * x1**3 + b1 * x1**2 + c1 * x1 + d1
            self.resultBox.append("One Intersect: \n (x: " + str(round(x1,2)) + ", y:" + str(round(y1,2)))
            plt.figure(num="Cubic Intercep")
            plt.plot(x*2,yf,'-r',label="Graph 1")
            plt.plot(x*2,ys,'limegreen',label="Graph 2")
            plt.axhline()
            plt.axvline()
            plt.scatter(x1,y1,color ="black")
            plt.xlabel('x', color='#1C2833')
            plt.ylabel('y',color='#1C2833')
            plt.legend(loc='upper left')
            plt.grid()
            plt.show()
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            y1 = a1 * x1 * x1 + b1 * x1 + c1*x1 + d1
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            y2 = a1 * x2**3 + b1 * x2**2 + c1*x1 + d1
            self.resultBox.append("Two Intersect: \n 1. (x: " + str(round(x1,2)) +", y: " + str(round(y1,2))) + "\n 2. (x: " + str(round(x2,2)) +", y: " + str(round(y2,2))))
            plt.figure(num="Cubic Intercept")
            plt.plot(x*2,yf,'-r',label="Graph 1")
            plt.plot(x*2,ys,'limegreen',label="Graph 2")
            plt.axhline()
            plt.axvline()
            plt.scatter(x1,y1,color ="black")
            plt.scatter(x2,y2,color="darkblue")
            plt.xlabel('x', color='#1C2833')
            plt.ylabel('y',color='#1C2833')
            plt.legend(loc='upper left')
            plt.grid()
            plt.show()


~                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
~                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
~                                   
