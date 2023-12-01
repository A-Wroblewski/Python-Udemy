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
    QPushButton, QSizePolicy, QWidget)

class Ui_central_widget(object):
    def setupUi(self, central_widget):
        if not central_widget.objectName():
            central_widget.setObjectName(u"central_widget")
        central_widget.resize(803, 474)
        font = QFont()
        font.setPointSize(36)
        central_widget.setFont(font)
        self.horizontalLayout = QHBoxLayout(central_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.grid_layout = QGridLayout()
        self.grid_layout.setObjectName(u"grid_layout")
        self.label_2 = QLabel(central_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.grid_layout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_1 = QLabel(central_widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.grid_layout.addWidget(self.label_1, 0, 0, 1, 1)

        self.push_button_1 = QPushButton(central_widget)
        self.push_button_1.setObjectName(u"push_button_1")

        self.grid_layout.addWidget(self.push_button_1, 1, 0, 1, 1)

        self.push_button_2 = QPushButton(central_widget)
        self.push_button_2.setObjectName(u"push_button_2")

        self.grid_layout.addWidget(self.push_button_2, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.grid_layout)


        self.retranslateUi(central_widget)

        QMetaObject.connectSlotsByName(central_widget)
    # setupUi

    def retranslateUi(self, central_widget):
        central_widget.setWindowTitle(QCoreApplication.translate("central_widget", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("central_widget", u"label2", None))
        self.label_1.setText(QCoreApplication.translate("central_widget", u"label1", None))
        self.push_button_1.setText(QCoreApplication.translate("central_widget", u"button1", None))
        self.push_button_2.setText(QCoreApplication.translate("central_widget", u"button2", None))
    # retranslateUi

