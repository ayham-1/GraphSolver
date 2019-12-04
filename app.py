from PyQt5 import QtWidgets
from ui.mainWindow import mainWin


def main():
    app = QtWidgets.QApplication([])
    window = mainWin()
    app.exec_()
    exit(0)


if __name__ == '__main__':
    main()
