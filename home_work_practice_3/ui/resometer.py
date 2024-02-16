# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resometer.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLCDNumber, QLabel,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(227, 157)
        Form.setMinimumSize(QSize(227, 157))
        Form.setMaximumSize(QSize(227, 157))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.spinBoxDelay = QSpinBox(Form)
        self.spinBoxDelay.setObjectName(u"spinBoxDelay")

        self.horizontalLayout.addWidget(self.spinBoxDelay)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lcdNumberCpu = QLCDNumber(Form)
        self.lcdNumberCpu.setObjectName(u"lcdNumberCpu")

        self.horizontalLayout_2.addWidget(self.lcdNumberCpu)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lcdNumberRam = QLCDNumber(Form)
        self.lcdNumberRam.setObjectName(u"lcdNumberRam")

        self.horizontalLayout_3.addWidget(self.lcdNumberRam)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"resometer", None))
        self.label.setText(QCoreApplication.translate("Form", u"delay", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"cpu util", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ramutil", None))
    # retranslateUi

