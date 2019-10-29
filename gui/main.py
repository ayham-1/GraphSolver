from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.pyplot import *
from linear import *
import numpy as np
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graph Solver")
        self.setGeometry(50, 50, 500, 500)
        self.setWindowIcon(QIcon('.\icons\window_icon.png'))
        self.Ui()

    def Ui(self):
        # font
        font = QFont()
        font.setPointSize(16)
        # combo box
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(QRect(105, 200, 300, 50))
        self.combo_box.addItem("Linear")
        self.combo_box.addItem("Linear Intersect")
        self.combo_box.setFont(font)
        # button
        self.run_button = QPushButton('Run', self)
        self.run_button.setGeometry(QRect(105, 375, 250, 50))
        self.run_button.setFont(font)
        self.run_button.clicked.connect(self.window_starter)
        self.show()

    def window_starter(self):
        self.window = QMainWindow()
        self.ui = Window_linear()
        self.ui.setupUi(self.window)
        self.window.show()


def main():
    app = QApplication(sys.argv)
    window_one = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
