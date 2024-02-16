# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weathermeter.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(381, 409)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEditlat = QLineEdit(self.groupBox)
        self.lineEditlat.setObjectName(u"lineEditlat")

        self.horizontalLayout_2.addWidget(self.lineEditlat)

        self.lineEditlong = QLineEdit(self.groupBox)
        self.lineEditlong.setObjectName(u"lineEditlong")

        self.horizontalLayout_2.addWidget(self.lineEditlong)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBoxDelay = QComboBox(self.groupBox)
        self.comboBoxDelay.setObjectName(u"comboBoxDelay")

        self.horizontalLayout.addWidget(self.comboBoxDelay)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.textEditWeather = QTextEdit(self.groupBox)
        self.textEditWeather.setObjectName(u"textEditWeather")

        self.verticalLayout_2.addWidget(self.textEditWeather)

        self.pushButtonGetW = QPushButton(self.groupBox)
        self.pushButtonGetW.setObjectName(u"pushButtonGetW")
        self.pushButtonGetW.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButtonGetW)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Weathermeter", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Settings", None))
        self.lineEditlat.setPlaceholderText(QCoreApplication.translate("Form", u"latitude", None))
        self.lineEditlong.setPlaceholderText(QCoreApplication.translate("Form", u"longitude", None))
        self.label.setText(QCoreApplication.translate("Form", u"delay", None))
        self.comboBoxDelay.setPlaceholderText("")
        self.pushButtonGetW.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u043f\u043e\u0433\u043e\u0434\u0443", None))
    # retranslateUi

