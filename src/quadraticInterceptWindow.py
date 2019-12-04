from PyQt5 import QtWidgets, uic
import math


class quadraticInterceptWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(quadraticInterceptWin, self).__init__()
        self.ui = uic.loadUi("ui/quadraticInterceptWindow.ui", self)

        # Get calcBtn, and connect it to stuff.
        self.calcBtn = self.findChild(QtWidgets.QPushButton, "calcBtn")
        self.calcBtn.clicked.connect(self.calcBtnPressed)

        # Get line1aBox
        self.line1aBox = self.findChild(QtWidgets.QLineEdit, "line1aBox")
        # Get line1bBox
        self.line1bBox = self.findChild(QtWidgets.QLineEdit, "line1bBox")
        # Get line1cBox
        self.line1cBox = self.findChild(QtWidgets.QLineEdit, "line1cBox")

        # Get line2aBox
        self.line2aBox = self.findChild(QtWidgets.QLineEdit, "line2aBox")
        # Get line2bBox
        self.line2bBox = self.findChild(QtWidgets.QLineEdit, "line2bBox")
        # Get line2cBox
        self.line2cBox = self.findChild(QtWidgets.QLineEdit, "line2cBox")

        # Get resultBox
        self.resultBox = self.findChild(QtWidgets.QTextEdit, "resultBox")

        self.ui.show()

    def calcBtnPressed(self):
        a1 = int(self.line1aBox.text())
        b1 = int(self.line1bBox.text())
        c1 = int(self.line1cBox.text())
        a2 = int(self.line2aBox.text())
        b2 = int(self.line2bBox.text())
        c2 = int(self.line2cBox.text())

        a = a2 - a1
        b = b2 - b1
        c = c2 - c1

        if a == 0.0 and b == 0.0 and c == 0.0:
            self.resultBox.append(
                "These Two parabolas are the same \n All points interset.")
            return

        if a == 0.0:
            if b == 0.0:
                self.resultBox.append("These two parabolas do not intersect.")
                return
            else:
                x1 = -c / b
                y1 = a1 * x1 * x1 + b1 * x1 + c1
                self.resutlBox.append("One Intersect: \n (x: " + str(x1) +
                                      ", y:" + str(y1))
                return
        discriminant = b * b - 4 * a * c

        if discriminant < 0.0:
            self.resutlBox.append("These two parabolas do not intersect.")
            return
        elif discriminant == 0.0:
            x1 = -b / (2 * a)
            y1 = a1 * x1 * x1 + b1 * x1 + c1
            self.resutlBox.append("One Intersect: \n (x: " + str(x1) + ", y:" +
                                  str(y1))
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            y1 = a1 * x1 * x1 + b1 * x1 + c1
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            y2 = a1 * x2 * x2 + b1 * x2 + c1
            self.resutlBox.append("Two Intersect: \n 1. (x: " + str(x1) +
                                  ", y: " + str(y1) + "\n 2. (x: " + str(x2) +
                                  ", y: " + str(y2))
