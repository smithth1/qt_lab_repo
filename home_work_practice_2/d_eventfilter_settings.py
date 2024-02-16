"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QSettings
from ui.d_eventfilter_settings import Ui_Form

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.ui.comboBox.addItems(["Dec", "Hex", "Bin", "Oct"])
        self.ui.dial.setMaximum(31)
        self.ui.horizontalSlider.setMaximum(31)
        self.load()

    def load(self) -> None:
        """
        load settings
        :return:
        """
        settings = QSettings("OrgName", "AppName")
        saved_value = settings.value("dialValue", 0)
        self.ui.dial.setValue(int(saved_value))
        saved_value = settings.value("ns", 0)
        self.ui.comboBox.setCurrentIndex(int(saved_value))


    def initSignals(self) -> None:
        """
        signals init
        :return:
        """
        self.ui.comboBox.currentIndexChanged.connect(self.onComboBoxChanged)
        self.ui.dial.valueChanged.connect(self.onDialValueChanged)
        self.ui.horizontalSlider.valueChanged.connect(self.onSliderValueChanged)

    def keyPressEvent(self, event) -> None:
        """
        event for key + - pressed
        :param event:
        :return:
        """
        if event.key() == Qt.Key_Plus:
            self.ui.dial.setValue(self.ui.dial.value() + 1)
        elif event.key() == Qt.Key_Minus:
            self.ui.dial.setValue(self.ui.dial.value() - 1)

    def closeEvent(self, event):
        settings = QSettings("OrgName", "AppName")
        settings.setValue("dialValue", self.ui.dial.value())
        settings.setValue("ns", self.ui.comboBox.currentIndex())

    def onComboBoxChanged(self) -> None:
        """
        slot for combobox
        :return:
        """
        if self.ui.comboBox.currentIndex() == 0:
            self.ui.lcdNumber.setMode (self.ui.lcdNumber.Mode.Dec)
        elif self.ui.comboBox.currentIndex() == 1:
            self.ui.lcdNumber.setMode(self.ui.lcdNumber.Mode.Hex)
        elif self.ui.comboBox.currentIndex() == 2:
            self.ui.lcdNumber.setMode(self.ui.lcdNumber.Mode.Bin)
        elif self.ui.comboBox.currentIndex() == 3:
            self.ui.lcdNumber.setMode(self.ui.lcdNumber.Mode.Oct)

    def onDialValueChanged(self) -> None:
        """
        slot for dial
        :return:
        """
        print("dial has value:", self.ui.dial.value())
        self.ui.lcdNumber.display(self.ui.dial.value())
        self.ui.horizontalSlider.setValue(self.ui.dial.value())
    def onSliderValueChanged(self) -> None:
        """
        slot for slider
        :return:
        """
        print("dial has value:", self.ui.horizontalSlider.value())
        self.ui.lcdNumber.display(self.ui.horizontalSlider.value())
        self.ui.dial.setValue(self.ui.horizontalSlider.value())

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
