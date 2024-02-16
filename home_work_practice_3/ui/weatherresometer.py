# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weatherresometer.ui'
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
    QLCDNumber, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(498, 604)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.spinBoxDelay = QSpinBox(Form)
        self.spinBoxDelay.setObjectName(u"spinBoxDelay")

        self.horizontalLayout_5.addWidget(self.spinBoxDelay)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lcdNumberCpu = QLCDNumber(Form)
        self.lcdNumberCpu.setObjectName(u"lcdNumberCpu")
        self.lcdNumberCpu.setMinimumSize(QSize(110, 53))

        self.horizontalLayout_4.addWidget(self.lcdNumberCpu)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lcdNumberRam = QLCDNumber(Form)
        self.lcdNumberRam.setObjectName(u"lcdNumberRam")
        self.lcdNumberRam.setMinimumSize(QSize(110, 53))

        self.horizontalLayout_3.addWidget(self.lcdNumberRam)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEditlat = QLineEdit(self.groupBox)
        self.lineEditlat.setObjectName(u"lineEditlat")
        self.lineEditlat.setEnabled(True)

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


        self.verticalLayout_3.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Weathermeter", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"delay", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"cpu util", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ram util", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Settings", None))
        self.lineEditlat.setPlaceholderText(QCoreApplication.translate("Form", u"latitude", None))
        self.lineEditlong.setPlaceholderText(QCoreApplication.translate("Form", u"longitude", None))
        self.label.setText(QCoreApplication.translate("Form", u"delay", None))
        self.comboBoxDelay.setPlaceholderText("")
        self.pushButtonGetW.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u043f\u043e\u0433\u043e\u0434\u0443", None))
    # retranslateUi

