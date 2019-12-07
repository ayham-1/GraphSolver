from PyQt5 import QtWidgets, uic
import matplotlib.pyplot as plt
import numpy as np

class cubicWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(cubicWin,self).__init__()
        self.ui = uic.loadUi("ui/cubicWindow.ui", self)

        # Get calcBtn, and connect it to stuff.
        self.calcBtn = self.findChild(QtWidgets.QPushButton, "calcBtn")
        self.calcBtn.clicked.connect(self.calcBtnPressed)

        # Get aBox, and connect it to stuff.
        self.aBox = self.findChild(QtWidgets.QLineEdit, "aBox")
        # Get bBox, and connect it to stuff.
        self.bBox = self.findChild(QtWidgets.QLineEdit, "bBox")
        # Get cBox, and connect it to stuff.
        self.cBox = self.findChild(QtWidgets.QLineEdit, "cBox")
        # Get dBox, and connect it to stuff.
        self.dBox = self.findChild(QtWidgets.QLineEdit, "dBox")

        self.ui.show()

    def calcBtnPressed(self):
        a = float(self.aBox.text())
        b = float(self.bBox.text())
        c = float(self.cBox.text())
        d = float(self.dBox.text())

        x = np.linspace(-10,10,100)
        y = a * x**3 + b * x + c * x + d

        plt.figure(num="Cubic Graph")
        graph = "y="  +str(a) + 'x^3 + ' + str(b) + '*x^2 + ' + str(c) + str(d)
        plt.title("Graph of " + graph)
        plt.plot(x,y,'-r',label=graph)
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc="upper left")
        plt.axhline()
        plt.axvline()
        plt.grid()
        plt.show()
~                    
