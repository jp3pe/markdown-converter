import sys

import PySide2
from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from UiMainWindow import Ui_MainWindow


def string_index_replacer(previous: str, incoming: str, index: int) -> str:
    result = previous[:index]
    result = result + incoming + previous[index + 1:]

    return result


class MainWindow(QtWidgets.QMainWindow):
    event = PySide2.QtGui.QDropEvent

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Buttons
        # Connect plain text to Slot
        self.button_plain_text = self.findChild(QtWidgets.QPushButton, 'pushButton_PlainText')
        self.button_plain_text.clicked.connect(self.push_button_plain_text)

        # Connect h1 buttons to Slot
        self.button_h1 = self.findChild(QtWidgets.QPushButton, 'pushButton_H1')
        self.button_h1.clicked.connect(self.push_button_h1)

        self.button_h2 = self.findChild(QtWidgets.QPushButton, 'pushButton_H2')
        self.button_h2.clicked.connect(self.push_button_h2)

        self.button_h3 = self.findChild(QtWidgets.QPushButton, 'pushButton_H3')
        self.button_h3.clicked.connect(self.push_button_h3)

        self.button_h4 = self.findChild(QtWidgets.QPushButton, 'pushButton_H4')
        self.button_h4.clicked.connect(self.push_button_h4)

        self.button_h5 = self.findChild(QtWidgets.QPushButton, 'pushButton_H5')
        self.button_h5.clicked.connect(self.push_button_h5)

        self.button_h6 = self.findChild(QtWidgets.QPushButton, 'pushButton_H6')
        self.button_h6.clicked.connect(self.push_button_h6)

        self.button_unordered_list = self.findChild(QtWidgets.QPushButton, 'pushButton_UnorderedList')
        self.button_unordered_list.clicked.connect(self.push_button_unordered_list)

        self.button_ordered_list = self.findChild(QtWidgets.QPushButton, 'pushButton_OrderedList')
        self.button_ordered_list.clicked.connect(self.push_button_ordered_list)

        # Editor
        # Connect text editor to Slot
        self.edit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
        self.edit.selectionChanged.connect(self.handle_selection_changed)

    @Slot()
    def handle_selection_changed(self):
        cursor = self.edit.textCursor()
        self.cursor_start = cursor.selectionStart()
        self.cursor_end = cursor.selectionEnd()

    @Slot()
    def push_button_plain_text(self):
        # Delete dragged string's markdown style from text editor
        previous_text: str = self.edit.toPlainText()
        self.style_remover(previous_text)

    @Slot()
    def push_button_h1(self):
        self.h_styler(1)

    @Slot()
    def push_button_h2(self):
        self.h_styler(2)

    @Slot()
    def push_button_h3(self):
        self.h_styler(3)

    @Slot()
    def push_button_h4(self):
        self.h_styler(4)

    @Slot()
    def push_button_h5(self):
        self.h_styler(5)

    @Slot()
    def push_button_h6(self):
        self.h_styler(6)

    @Slot()
    def push_button_unordered_list(self, prefix: str):
        self.list_styler('*')

    @Slot()
    def push_button_ordered_list(self, prefix: str):
        self.list_styler('1.')

    # Method to insert prefix string like H1~H6's prefix('#') and lists' prefixes('*', '1.')
    def insert_prefix(self, prefix: str, previous_text) -> str:
        # When user don't dragged any string
        if self.cursor_start == self.cursor_end:
            return previous_text

        # drag started from 0 index
        if self.cursor_start <= 0:
            # return prefix + user_input
            changed_text = prefix + ' ' + previous_text[self.cursor_start:]
        # drag start from bigger than 0 index
        elif self.cursor_start > 0:
            # return user input + prefix + behind user's dragged string
            changed_text = previous_text[:self.cursor_start] + prefix + ' ' + previous_text[self.cursor_start:]

        return changed_text

    def h_styler(self, h_num: int):
        # Change selected_text in previous text
        # And replace plain text of edit with it.
        previous_text: str = self.edit.toPlainText()
        changed_text = self.insert_prefix('#' * h_num, previous_text)
        self.edit.setPlainText(changed_text)

    # method to call insert_prefix to insert prefix with list_prefixes
    def list_styler(self, prefix: str):
        # Change selected_text in previous text
        # And replace plain text of edit with it.
        previous_text: str = self.edit.toPlainText()
        changed_text = self.insert_prefix(prefix, previous_text)
        self.edit.setPlainText(changed_text)

    # method to insert '* ' or '1. ' for ordered list and unordered list
    def list_insert(self, prefix: str):
        pass

    def style_remover(self, previous_text: str):
        # drag started from 0 index
        temp_text: str = previous_text
        i = 0
        if self.cursor_start <= 0:
            # header delete
            if temp_text[i] == '#':
                while temp_text[i] == '#':
                    temp_text = string_index_replacer(temp_text, '', i)

                i = 0

            # lists delete
            if temp_text[i:i + 2] == '1.':
                # call string_index_replacer twice to remove number and dot
                temp_text = string_index_replacer(temp_text, '', i)
                temp_text = string_index_replacer(temp_text, '', i)
            if temp_text[i] == '*':
                temp_text = string_index_replacer(temp_text, '', i)

            if temp_text[i] == ' ':
                temp_text = string_index_replacer(temp_text, '', i)
                changed_text = temp_text

            self.edit.setPlainText(changed_text)

        # drag start from bigger than 0 index
        elif self.cursor_start > 0:
            changed_text = previous_text[:self.cursor_start]
            # set index to point cursor start
            i = self.cursor_start

            while temp_text[i] == '#':
                temp_text = string_index_replacer(temp_text, '', i)

            # lists delete
            if temp_text[i:i + 2] == '1.':
                # call string_index_replacer twice to remove number and dot
                temp_text = string_index_replacer(temp_text, '', i)
                temp_text = string_index_replacer(temp_text, '', i)
            if temp_text[i] == '*':
                temp_text = string_index_replacer(temp_text, '', i)

            if temp_text[i] == ' ':
                temp_text = string_index_replacer(temp_text, '', i)
                changed_text = changed_text + temp_text[self.cursor_start:]

            self.edit.setPlainText(changed_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
