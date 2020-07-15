import re
import sys

import PySide2
from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from UiMainWindow import Ui_MainWindow


def string_index_replacer(previous: str, incoming: str, index: int) -> str:
    result = previous[:index]
    result = result + incoming + previous[index + 1:]

    return result


def space_remover(temp_text: str, i: int) -> str:
    if temp_text[i] == ' ':
        temp_text = string_index_replacer(temp_text, '', i)
        changed_text = temp_text

        return changed_text


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

        # Connect header buttons to Slot method
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

        self.button_bold = self.findChild(QtWidgets.QPushButton, 'pushButton_Bold')
        self.button_bold.clicked.connect(self.push_button_bold)

        self.button_italic = self.findChild(QtWidgets.QPushButton, 'pushButton_Italic')
        self.button_italic.clicked.connect(self.push_button_italic)

        self.button_ordered_list = self.findChild(QtWidgets.QPushButton, 'pushButton_OrderedList')
        self.button_ordered_list.clicked.connect(self.push_button_ordered_list)

        self.button_unordered_list = self.findChild(QtWidgets.QPushButton, 'pushButton_UnorderedList')
        self.button_unordered_list.clicked.connect(self.push_button_unordered_list)

        self.button_link = self.findChild(QtWidgets.QPushButton, 'pushButton_Link')
        self.button_link.clicked.connect(self.push_button_link)

        self.button_image = self.findChild(QtWidgets.QPushButton, 'pushButton_Image')
        self.button_image.clicked.connect(self.push_button_image)

        self.button_block_quote = self.findChild(QtWidgets.QPushButton, 'pushButton_BlockQuote')
        self.button_block_quote.clicked.connect(self.push_button_block_quote)

        self.button_inline_code = self.findChild(QtWidgets.QPushButton, 'pushButton_InlineCode')
        self.button_inline_code.clicked.connect(self.push_button_inline_code)

        # Editor
        # Connect text editor to Slot
        self.edit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
        self.edit.selectionChanged.connect(self.handle_selection_changed)

    # Get mouse cursor start and end position from text editor
    @Slot()
    def handle_selection_changed(self):
        cursor = self.edit.textCursor()
        self.cursor_start = cursor.selectionStart()
        self.cursor_end = cursor.selectionEnd()

    # Delete dragged string's markdown style from text editor
    @Slot()
    def push_button_plain_text(self):
        previous_text: str = self.edit.toPlainText()
        self.style_remover(previous_text)

    # Call prefix_styler method to add '#'s
    @Slot()
    def push_button_h1(self):
        self.prefix_styler('#', True)

    @Slot()
    def push_button_h2(self):
        self.prefix_styler('##', True)

    @Slot()
    def push_button_h3(self):
        self.prefix_styler('###', True)

    @Slot()
    def push_button_h4(self):
        self.prefix_styler('####', True)

    @Slot()
    def push_button_h5(self):
        self.prefix_styler('#####', True)

    @Slot()
    def push_button_h6(self):
        self.prefix_styler('######', True)

    @Slot()
    def push_button_bold(self):
        # Save current cursor location to prevent initialize after using it from method
        temp_cursor_start = self.cursor_start
        temp_cursor_end = self.cursor_end
        self.prefix_styler('**', False)

        # Modify cursor's start index after add '**'
        self.cursor_start = temp_cursor_start + 2
        self.cursor_end = temp_cursor_end + 2
        self.suffix_styler('**', False)

    @Slot()
    def push_button_italic(self):
        # Save current cursor location to prevent initialize after using it from method
        temp_cursor_start = self.cursor_start
        temp_cursor_end = self.cursor_end

        # Modify cursor's start index after add '*'
        self.prefix_styler('*', False)
        self.cursor_start = temp_cursor_start + 1
        self.cursor_end = temp_cursor_end + 1
        self.suffix_styler('*', False)

    @Slot()
    def push_button_ordered_list(self):
        self.prefix_styler('1.', True)

    @Slot()
    def push_button_unordered_list(self):
        self.prefix_styler('*', True)

    @Slot()
    def push_button_link(self):
        self.link_styler()

    @Slot()
    def push_button_image(self):
        self.image_styler()

    @Slot()
    def push_button_block_quote(self):
        self.prefix_styler('>', True)

    @Slot()
    def push_button_inline_code(self):
        # Save current cursor location to prevent initialize after using it from method
        temp_cursor_start = self.cursor_start
        temp_cursor_end = self.cursor_end

        # Modify cursor's start index after add '*'
        self.prefix_styler('`', True)
        self.cursor_start = temp_cursor_start + 2
        self.cursor_end = temp_cursor_end + 2
        self.suffix_styler('`', True)

    # Method to return string from editor
    def get_editor_text(self) -> str:
        text_result: str = self.edit.toPlainText()

        return text_result

    # Method to insert prefix string
    def insert_prefix(self, prefix: str, previous_text: str, space: bool) -> str:
        # When user didn't drag any string in the editor
        if self.cursor_start == self.cursor_end:
            return previous_text

        # When dragging started from 0 index
        if self.cursor_start <= 0:
            # Return prefix + user's input text from editor
            if space:
                changed_text = prefix + ' ' + previous_text[self.cursor_start:]
            else:
                changed_text = prefix + previous_text[self.cursor_start:]
        # When dragging start from bigger than 0 index
        elif self.cursor_start > 0:
            # Return user's input text from text editor before dragged + prefix + behind user's dragged string
            if space:
                changed_text = previous_text[:self.cursor_start] + prefix + ' ' + previous_text[self.cursor_start:]
            else:
                changed_text = previous_text[:self.cursor_start] + prefix + previous_text[self.cursor_start:]

        return changed_text

    # Method to insert suffix string
    def insert_suffix(self, suffix: str, previous_text: str, space: bool) -> str:
        # When user didn't drag any string
        if self.cursor_start == self.cursor_end:
            return previous_text

        # When dragging started from 0 index
        if self.cursor_start <= 0:
            # Return user's input from text editor + suffix
            if space:
                changed_text = previous_text[:self.cursor_end] + suffix + ' ' + previous_text[self.cursor_end:]
            else:
                changed_text = previous_text[:self.cursor_end] + suffix + previous_text[self.cursor_end:]
        # When dragging started from bigger than 0 index
        elif self.cursor_start > 0:
            # Return user input from text editor before dragged + suffix + behind user's dragged string
            if space:
                changed_text = previous_text[:self.cursor_start] + \
                               previous_text[self.cursor_start:self.cursor_end]
                changed_text = changed_text + suffix + ' ' + previous_text[self.cursor_end:]
            else:
                changed_text = previous_text[:self.cursor_start] + \
                               previous_text[self.cursor_start:self.cursor_end]
                changed_text = changed_text + suffix + previous_text[self.cursor_end:]

        return changed_text

    # Method to insert link format
    def insert_link(self, previous_text: str, image: bool) -> str:
        # When dragging started from 0 index
        if self.cursor_start <= 0:
            if image:
                changed_text = '![Explanation about image](image\'s local path or web path starting http, https)\n' + \
                               previous_text
            else:
                changed_text = '[Explanation about website](http://example.com)' + previous_text
            # When dragging started from bigger than 0 index
        elif self.cursor_start > 0:
            if image:
                changed_text = previous_text[:self.cursor_start] + \
                               '![Explanation about image](image\'s local path or web path starting http, https)\n' + \
                               previous_text[self.cursor_start:]
            else:
                changed_text = previous_text[:self.cursor_start] + '[Explanation about website](http://example.com)' + \
                               previous_text[self.cursor_start:]

        return changed_text

    def style_remover(self, previous_text: str):
        temp_text: str = previous_text
        # When dragging started from 0 index
        if self.cursor_start <= 0:
            i = 0
            # Header delete
            if temp_text[i] == '#':
                while temp_text[i] == '#':
                    temp_text = string_index_replacer(temp_text, '', i)
                i = 0

                temp_text = space_remover(temp_text, i)

            # Bold delete
            if temp_text[i:i + 2] == '**' and temp_text[self.cursor_end - 2:self.cursor_end] == '**':
                # Delete prefix style
                temp_text = string_index_replacer(temp_text, '', i)
                temp_text = string_index_replacer(temp_text, '', i)

                # Delete suffix style
                temp_text = string_index_replacer(temp_text, '', self.cursor_end - 4)
                temp_text = string_index_replacer(temp_text, '', self.cursor_end - 4)

            # Italic delete
            if temp_text[i: i + 1] == '*' and temp_text[self.cursor_end - 1:self.cursor_end] == '*':
                # Delete prefix style
                temp_text = string_index_replacer(temp_text, '', i)

                # Delete suffix style
                temp_text = string_index_replacer(temp_text, '', self.cursor_end - 2)

            # Ordered list delete
            if temp_text[i:i + 2] == '1.':
                # call string_index_replacer twice to remove number and dot
                temp_text = string_index_replacer(temp_text, '', i)
                temp_text = string_index_replacer(temp_text, '', i)
                temp_text = space_remover(temp_text, i)

            # Unordered list delete
            if temp_text[i] == '*':
                temp_text = string_index_replacer(temp_text, '', i)
                temp_text = space_remover(temp_text, i)

            # Link delete
            # [GitHub](http://github.com)
            # link_regex = re.compile('^(\[\w+\]\(http://|(https://[\w+.]\))')
            # if link_regex.match(temp_text[i]):
            #     temp_text = re.sub(link_regex, '', temp_text)

            changed_text = temp_text
            self.edit.setPlainText(changed_text)

        # When dragging started from bigger than 0 index
        elif self.cursor_start > 0:
            changed_text = previous_text[:self.cursor_start]
            # Set index to cursor start
            i = self.cursor_start

            # Header delete
            if temp_text[i] == '#':
                while temp_text[i] == '#':
                    temp_text = string_index_replacer(temp_text, '', i)

                temp_text = space_remover(temp_text, i)

            # Bold delete
            if temp_text[i:i + 2] == '**' and temp_text[self.cursor_end - 2:self.cursor_end] == '**':
                # Delete prefix style
                temp_text = string_index_replacer(temp_text, '', i)
                temp_text = string_index_replacer(temp_text, '', i)

                # Delete suffix style
                temp_text = string_index_replacer(temp_text, '', self.cursor_end - 4)
                temp_text = string_index_replacer(temp_text, '', self.cursor_end - 4)

            # Italic delete
            if temp_text[i: i + 1] == '*' and temp_text[self.cursor_end - 1:self.cursor_end] == '*':
                # Delete prefix style
                temp_text = string_index_replacer(temp_text, '', i)

                # Delete suffix style
                temp_text = string_index_replacer(temp_text, '', self.cursor_end - 2)

            # Ordered list delete
            if temp_text[i:i + 2] == '1.':
                # call string_index_replacer twice to remove number and dot
                temp_text = string_index_replacer(temp_text, '', i)
                temp_text = string_index_replacer(temp_text, '', i)
                temp_text = space_remover(temp_text, i)

            # Unordered list delete
            if temp_text[i] == '*':
                temp_text = string_index_replacer(temp_text, '', i)
                temp_text = space_remover(temp_text, i)

            changed_text = temp_text
            self.edit.setPlainText(changed_text)

    # Method to call insert_prefix and apply prefix to text editor
    def prefix_styler(self, prefix: str, space: bool):
        previous_text: str = self.get_editor_text()
        if space:
            changed_text = self.insert_prefix(prefix, previous_text, True)
        else:
            changed_text = self.insert_prefix(prefix, previous_text, False)

        self.edit.setPlainText(changed_text)

    # Method to call insert_suffix and apply suffix to text editor
    def suffix_styler(self, suffix: str, space: bool):
        previous_text: str = self.get_editor_text()
        if space:
            changed_text = self.insert_suffix(suffix, previous_text, True)
        else:
            changed_text = self.insert_suffix(suffix, previous_text, False)

        self.edit.setPlainText(changed_text)

    # Method to call link_insert and apply link to text editor
    def link_styler(self):
        previous_text: str = self.get_editor_text()

        changed_text = self.insert_link(previous_text, False)

        self.edit.setPlainText(changed_text)

    # Method to call image_insert and apply image to text editor
    def image_styler(self):
        previous_text: str = self.get_editor_text()

        changed_text = self.insert_link(previous_text, True)

        self.edit.setPlainText(changed_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
