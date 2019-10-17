from PyQt5 import QtWidgets, uic
from methods.linear.calcLinear import Linear
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/main.ui', self)
        # Search for run button
        a, c, length = self.getNumbers()
        self.linear = Linear(a, c, length)
        self.button = self.findChild(QtWidgets.QPushButton, 'run_button')
        self.button.clicked.connect(self.linear.calc_linear_line)

        self.show()

    def getNumbers(self):
        a = int(input("Value for a: "))
        c = int(input("Value for c: "))
        length = int(input("Value for length: "))
        return a, c, length


app = QtWidgets.QApplication([])
window = Ui()
app.exec_()
exit(0)
