import sys

import PySide2
from PySide2 import QtWidgets
from PySide2.QtCore import Slot

from UiMainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    event = PySide2.QtGui.QDropEvent

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.button_h1 = self.findChild(QtWidgets.QPushButton, 'pushButton_H1')
        self.button_h1.clicked.connect(self.push_button_h1)
        self.edit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
        self.edit.selectionChanged.connect(self.handle_selection_changed)

    @Slot()
    def push_button_h1(self):
        print("push_button_h1 method worked")

    @Slot()
    def handle_selection_changed(self):
        cursor = self.edit.textCursor()
        print("Selection start: %d end: %d" %
              (cursor.selectionStart(), cursor.selectionEnd()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
