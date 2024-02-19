# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sysinfo_main.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLCDNumber, QLabel, QProgressBar, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(818, 587)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.spinBoxDelay = QSpinBox(Form)
        self.spinBoxDelay.setObjectName(u"spinBoxDelay")
        self.spinBoxDelay.setMinimumSize(QSize(50, 0))
        self.spinBoxDelay.setMinimum(5)
        self.spinBoxDelay.setMaximum(30)
        self.spinBoxDelay.setSingleStep(5)

        self.horizontalLayout.addWidget(self.spinBoxDelay)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_10 = QHBoxLayout(self.tab)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lcdNumberCPU = QLCDNumber(self.groupBox)
        self.lcdNumberCPU.setObjectName(u"lcdNumberCPU")

        self.horizontalLayout_4.addWidget(self.lcdNumberCPU)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lcdNumberCPUCORES = QLCDNumber(self.groupBox)
        self.lcdNumberCPUCORES.setObjectName(u"lcdNumberCPUCORES")

        self.horizontalLayout_5.addWidget(self.lcdNumberCPUCORES)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lcdNumberCPUTHREADS = QLCDNumber(self.groupBox)
        self.lcdNumberCPUTHREADS.setObjectName(u"lcdNumberCPUTHREADS")

        self.horizontalLayout_6.addWidget(self.lcdNumberCPUTHREADS)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.lcdNumberRAMA = QLCDNumber(self.groupBox_2)
        self.lcdNumberRAMA.setObjectName(u"lcdNumberRAMA")

        self.horizontalLayout_7.addWidget(self.lcdNumberRAMA)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.lcdNumberRAMAV = QLCDNumber(self.groupBox_2)
        self.lcdNumberRAMAV.setObjectName(u"lcdNumberRAMAV")

        self.horizontalLayout_8.addWidget(self.lcdNumberRAMAV)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.lcdNumberRAMU = QLCDNumber(self.groupBox_2)
        self.lcdNumberRAMU.setObjectName(u"lcdNumberRAMU")

        self.horizontalLayout_9.addWidget(self.lcdNumberRAMU)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_8)

        self.progressBarBattery = QProgressBar(self.groupBox_3)
        self.progressBarBattery.setObjectName(u"progressBarBattery")
        self.progressBarBattery.setLayoutDirection(Qt.LeftToRight)
        self.progressBarBattery.setAutoFillBackground(False)
        self.progressBarBattery.setStyleSheet(u"")
        self.progressBarBattery.setValue(50)
        self.progressBarBattery.setTextVisible(True)
        self.progressBarBattery.setOrientation(Qt.Horizontal)
        self.progressBarBattery.setInvertedAppearance(False)

        self.verticalLayout_5.addWidget(self.progressBarBattery)


        self.verticalLayout_4.addWidget(self.groupBox_3)


        self.horizontalLayout_10.addLayout(self.verticalLayout_4)

        self.textEditSysInfo = QTextEdit(self.tab)
        self.textEditSysInfo.setObjectName(u"textEditSysInfo")
        self.textEditSysInfo.setMinimumSize(QSize(600, 0))
        self.textEditSysInfo.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.textEditSysInfo)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidgetServices = QTableWidget(self.tab_3)
        if (self.tableWidgetServices.columnCount() < 2):
            self.tableWidgetServices.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetServices.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetServices.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        if (self.tableWidgetServices.rowCount() < 2):
            self.tableWidgetServices.setRowCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidgetServices.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidgetServices.setVerticalHeaderItem(1, __qtablewidgetitem7)
        self.tableWidgetServices.setObjectName(u"tableWidgetServices")

        self.horizontalLayout_2.addWidget(self.tableWidgetServices)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"sysinfo", None))
        self.label.setText(QCoreApplication.translate("Form", u"delay", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"CPU", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"CPU UTIL%", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"CPU CORES", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"CPU THREADS", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"RAM", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ALL RAM", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"RAM AVAIL", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"RAMUTIL %", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Battery", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"BATTERY", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"SysInfo", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"NAME", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"123", None));
        ___qtablewidgetitem3 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"qwe", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Processes", None))
        ___qtablewidgetitem4 = self.tableWidgetServices.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"New Column", None));
        ___qtablewidgetitem5 = self.tableWidgetServices.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"New Column", None));
        ___qtablewidgetitem6 = self.tableWidgetServices.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidgetServices.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"New Row", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Services", None))
    # retranslateUi

