from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets, uic


class mainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainWin, self).__init__()
        self.ui = uic.loadUi("ui/mainWindow.ui")

        #self.runBtn = self.findChild(QWidget.QPushButton, "runBtn")

        self.ui.show()
