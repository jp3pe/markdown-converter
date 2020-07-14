# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 614)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionSave_as_md = QAction(MainWindow)
        self.actionSave_as_md.setObjectName(u"actionSave_as_md")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 141, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_PlainText = QPushButton(self.verticalLayoutWidget)
        self.pushButton_PlainText.setObjectName(u"pushButton_PlainText")

        self.verticalLayout.addWidget(self.pushButton_PlainText)

        self.pushButton_H1 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_H1.setObjectName(u"pushButton_H1")

        self.verticalLayout.addWidget(self.pushButton_H1)

        self.pushButton_H2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_H2.setObjectName(u"pushButton_H2")

        self.verticalLayout.addWidget(self.pushButton_H2)

        self.pushButton_H3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_H3.setObjectName(u"pushButton_H3")

        self.verticalLayout.addWidget(self.pushButton_H3)

        self.pushButton_H4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_H4.setObjectName(u"pushButton_H4")

        self.verticalLayout.addWidget(self.pushButton_H4)

        self.pushButton_H5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_H5.setObjectName(u"pushButton_H5")

        self.verticalLayout.addWidget(self.pushButton_H5)

        self.pushButton_H6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_H6.setObjectName(u"pushButton_H6")

        self.verticalLayout.addWidget(self.pushButton_H6)

        self.pushButton_Bold = QPushButton(self.verticalLayoutWidget)
        self.pushButton_Bold.setObjectName(u"pushButton_Bold")

        self.verticalLayout.addWidget(self.pushButton_Bold)

        self.pushButton_Italic = QPushButton(self.verticalLayoutWidget)
        self.pushButton_Italic.setObjectName(u"pushButton_Italic")

        self.verticalLayout.addWidget(self.pushButton_Italic)

        self.pushButton_OrderedList = QPushButton(self.verticalLayoutWidget)
        self.pushButton_OrderedList.setObjectName(u"pushButton_OrderedList")

        self.verticalLayout.addWidget(self.pushButton_OrderedList)

        self.pushButton_UnorderedList = QPushButton(self.verticalLayoutWidget)
        self.pushButton_UnorderedList.setObjectName(u"pushButton_UnorderedList")

        self.verticalLayout.addWidget(self.pushButton_UnorderedList)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(170, 10, 611, 531))
        self.horizontalScrollBar = QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setGeometry(QRect(170, 540, 611, 20))
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)
        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(780, 10, 20, 531))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 820, 22))
        self.menuMarkdown_converter = QMenu(self.menubar)
        self.menuMarkdown_converter.setObjectName(u"menuMarkdown_converter")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMarkdown_converter.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuMarkdown_converter.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionSave_as_md)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionSave_as_md.setText(QCoreApplication.translate("MainWindow", u"Save as .md", None))
        self.pushButton_PlainText.setText(QCoreApplication.translate("MainWindow", u"Plain Text", None))
        self.pushButton_H1.setText(QCoreApplication.translate("MainWindow", u"H1", None))
        self.pushButton_H2.setText(QCoreApplication.translate("MainWindow", u"H2", None))
        self.pushButton_H3.setText(QCoreApplication.translate("MainWindow", u"H3", None))
        self.pushButton_H4.setText(QCoreApplication.translate("MainWindow", u"H4", None))
        self.pushButton_H5.setText(QCoreApplication.translate("MainWindow", u"H5", None))
        self.pushButton_H6.setText(QCoreApplication.translate("MainWindow", u"H6", None))
        self.pushButton_Bold.setText(QCoreApplication.translate("MainWindow", u"Bold", None))
        self.pushButton_Italic.setText(QCoreApplication.translate("MainWindow", u"Italic", None))
        self.pushButton_OrderedList.setText(QCoreApplication.translate("MainWindow", u"OrderedList", None))
        self.pushButton_UnorderedList.setText(QCoreApplication.translate("MainWindow", u"UnorderedList", None))
        self.menuMarkdown_converter.setTitle(QCoreApplication.translate("MainWindow", u"Markdown converter", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

