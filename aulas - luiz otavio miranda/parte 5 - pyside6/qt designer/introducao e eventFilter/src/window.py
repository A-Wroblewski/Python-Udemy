# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1319, 813)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.full_grid_layout = QGridLayout()
        self.full_grid_layout.setObjectName(u"full_grid_layout")
        self.upper_label = QLabel(self.centralwidget)
        self.upper_label.setObjectName(u"upper_label")
        font = QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.upper_label.setFont(font)
        self.upper_label.setAlignment(Qt.AlignCenter)

        self.full_grid_layout.addWidget(self.upper_label, 0, 0, 1, 1)

        self.inner_grid_layout = QGridLayout()
        self.inner_grid_layout.setObjectName(u"inner_grid_layout")
        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.name_label.setFont(font1)

        self.inner_grid_layout.addWidget(self.name_label, 0, 0, 1, 1)

        self.name_input = QLineEdit(self.centralwidget)
        self.name_input.setObjectName(u"name_input")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        self.name_input.setFont(font2)
        self.name_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.inner_grid_layout.addWidget(self.name_input, 0, 1, 1, 1)

        self.name_button = QPushButton(self.centralwidget)
        self.name_button.setObjectName(u"name_button")
        font3 = QFont()
        font3.setPointSize(14)
        self.name_button.setFont(font3)

        self.inner_grid_layout.addWidget(self.name_button, 0, 2, 1, 1)


        self.full_grid_layout.addLayout(self.inner_grid_layout, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.full_grid_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1319, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.upper_label.setText(QCoreApplication.translate("MainWindow", u"Text\u00e3o", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Digite seu nome:", None))
        self.name_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digite aqui", None))
        self.name_button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

