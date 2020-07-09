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
        self.cursor_start: int
        self.cursor_end: int

        # Buttons
        # Connect h1 buttons to Slot
        self.button_h1 = self.findChild(QtWidgets.QPushButton, 'pushButton_H1')
        self.button_h1.clicked.connect(self.push_button_h1)

        # self.button_h2 = self.findChild(QtWidgets.QPushButton, 'pushButton_H2')
        # self.button_h2.clicked.connect(self.push_button_h2)
        #
        # self.button_h3 = self.findChild(QtWidgets.QPushButton, 'pushButton_H3')
        # self.button_h3.clicked.connect(self.push_button_h3)
        #
        # self.button_h4 = self.findChild(QtWidgets.QPushButton, 'pushButton_H4')
        # self.button_h4.clicked.connect(self.push_button_h4)
        #
        # self.button_h5 = self.findChild(QtWidgets.QPushButton, 'pushButton_H5')
        # self.button_h5.clicked.connect(self.push_button_h5)
        #
        # self.button_h6 = self.findChild(QtWidgets.QPushButton, 'pushButton_H6')
        # self.button_h6.clicked.connect(self.push_button_h6)

        # Editor
        # Connect text editor to Slot
        self.edit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
        self.edit.selectionChanged.connect(self.handle_selection_changed)

        # mouse cursor
        self.cursor = self.edit.textCursor()

    @Slot()
    def handle_selection_changed(self):
        cursor = self.edit.textCursor()
        self.cursor_start = cursor.selectionStart()
        self.cursor_end = cursor.selectionEnd()

    @Slot()
    def push_button_h1(self):
        previous_text: str = self.edit.toPlainText()
        selected_text = self.cursor

        # Change selected_text in previous text
        # And replace plain text of edit with it.
        # print(self.cursor_start)
        # print(self.cursor_end)

        if (self.cursor_start <= 0):
            changed_text = '# ' + previous_text[self.cursor_start:]
            print(changed_text)
        elif (self.cursor_start > 0):
            changed_text = previous_text[:self.cursor_start] + '# ' + previous_text[self.cursor_start:]
            print(changed_text)

        # changed_text = previous_text[:self.cursor_start] + \
        #                "# " \
        #                + selected_text + \
        #                self.cursor_end
        self.edit.setPlainText(changed_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
