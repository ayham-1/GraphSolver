from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.pyplot import *
import numpy as np
import sys


class Window_linear(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Linear Solver")
        self.setGeometry(50, 50, 500, 500)
        self.setWindowIcon(QIcon('.\icons\bar-graph-on-a-rectangle.png'))
        self.setupUi()

    def setupUi(self):
        # text boxes
        self.m_textbox = QLineEdit(self)
        self.m_textbox.move(100, 300)

        self.c_textbox = QLineEdit(self)
        self.c_textbox.move(100, 350)
        # button
        self.calc_button = QPushButton('Calculate', self)
        self.calc_button.move(300, 350)
        self.calc_button.clicked.connect(self.input_usage)
        # font
        font = QFont()
        font.setPointSize(14)
        # label
        self.m_label = QLabel(self)
        self.m_label.setText("M:")
        self.m_label.move(50, 300)
        self.m_label.setFont(font)

        self.c_label = QLabel(self)
        self.c_label.setText("C:")
        self.c_label.move(50, 350)
        self.c_label.setFont(font)
        self.show()

    def input_usage(self):

        m_input = int(self.m_textbox.text())
        c_input = int(self.c_textbox.text())

    def graph(self):
        pass

    def calcLinearLine(self, a, c, length):
        result = [(0-length, a*(0 - length)), (0-length, a*length)]
        return result


def main():
    app = QApplication(sys.argv)
    window_linear = Window_linear()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
