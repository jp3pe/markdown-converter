import sys

from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from UiMainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        button_h1 = self.findChild(QtWidgets.QPushButton, 'pushButton_H1')
        button_h1.clicked.connect(self.push_button_h1)

    @Slot()
    def push_button_h1(self):
        #         test push_button_h1
        print("push_button_h1 method worked")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
