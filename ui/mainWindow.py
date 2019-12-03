from PyQt5 import QtWidgets, uic


class mainWin(QtWidgets.QMainWindow):
    equval = "Linear"

    def __init__(self):
        super(mainWin, self).__init__()
        self.ui = uic.loadUi("ui/mainWindow.ui", self)

        # Get runBtn, and connect it to stuff.
        self.runBtn = self.findChild(QtWidgets.QPushButton, "runBtn")
        self.runBtn.clicked.connect(self.runBtnPressed)

        # Get equCbo, and connect it to stuff.
        self.equCbo = self.findChild(QtWidgets.QComboBox, "equCbo")
        self.equCbo.activated[str].connect(self.onEquCboChanged)

        self.ui.show()

    def runBtnPressed(self):
        print(self.equval)

    def onEquCboChanged(self, text):
        self.equval = text
