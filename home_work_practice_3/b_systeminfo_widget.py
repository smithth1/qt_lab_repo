"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
from PySide6 import QtWidgets, QtCore
from ui.resometer import Ui_Form
from a_threads import SystemInfo

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.spinBoxDelay.setMinimum(2)
        self.system_thread = SystemInfo()
        self.system_thread.delay = self.ui.spinBoxDelay.value()
        self.InitSignal()

    def InitSignal(self) -> None:
        self.ui.spinBoxDelay.valueChanged.connect(self.delay_time_changed)
        self.system_thread.systemSignal.connect(lambda data: self.info(data))


    def info(self, data: list):
        self.ui.lcdNumberCpu.display(data[0])
        self.ui.lcdNumberRam.display(data[1])


    def delay_time_changed(self):
        self.system_thread.delay = self.ui.spinBoxDelay.value()

        if self.system_thread.isRunning() == False:
            self.system_thread.start()



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()