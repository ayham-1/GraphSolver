from PyQt5 import QtWidgets, uic


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
        m1 = int(self.line1mBox.text())
        c1 = int(self.line1cBox.text())
        m2 = int(self.line2mBox.text())
        c2 = int(self.line2cBox.text())
        x = (c2 - c1) / (m1 - m2)
        y = m1 * x + c1
        self.resultXBox.setText(str(x))
        self.resultYBox.setText(str(y))
