"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов +
    * Текущее основное окно
    * Разрешение экрана +
    * На каком экране окно находится
    * Размеры окна +
    * Минимальные размеры окна
    * Текущее положение (координаты) окна+
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию +
    * При изменении размера окна выводить его новый размер +
"""


from PySide6 import QtWidgets, QtGui, QtCore
from ui.c_signals_events import Ui_Form
import time

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        gsi1 = QtCore.QCoreApplication.instance()
        screens = gsi1.screens()
        self.ui.plainTextEdit.appendPlainText(
            f'{self.getTimeNow()}: Количество мониторов = {len(screens)}')
        for screen in screens:
            self.ui.plainTextEdit.appendPlainText(
                f'{self.getTimeNow()}: Разрешение экрана {screen.name()}= {QtGui.QScreen.size(screen).width()},{QtGui.QScreen.size(screen).height()}')
        self.halfscreenres = [int(QtGui.QScreen.size(screen).width())/2,int(QtGui.QScreen.size(screen).height())/2]
        self.halfappsize = [int(self.geometry().width()/2), int(self.geometry().height()/2)]
        self.ui.plainTextEdit.appendPlainText(f'{self.getTimeNow()}: Размер окна = {self.geometry().width()},{self.geometry().height()}')
        self.ui.plainTextEdit.appendPlainText(f'{self.getTimeNow()}: Минимальный Размер окна = {self.minimumSize().width()},{self.minimumSize().height()}')
        self.ui.plainTextEdit.appendPlainText(f'{self.getTimeNow()}: координаты центра приложения {self.centerOfApp(self.halfappsize,self.halfscreenres)}')

    def getTimeNow(self) -> str:
        """
        function to get time
        :return:
        """
        timeNow = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
        return timeNow


    def centerOfApp(self, a, b) -> list:
        cntrapp = [b[0] - a[0], b[1] - a[1]]
        print(cntrapp)
        self.centerofapp = cntrapp
        return cntrapp

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonMoveCoords.clicked.connect(self.onpushButtonMoveCoordsClicked)
        self.ui.pushButtonLT.clicked.connect(self.onpushButtonLTClicked)
        self.ui.pushButtonLB.clicked.connect(self.onpushButtonLBClicked)
        self.ui.pushButtonRT.clicked.connect(self.onpushButtonRTClicked)
        self.ui.pushButtonRB.clicked.connect(self.onpushButtonRBClicked)
        self.ui.pushButtonCenter.clicked.connect(self.onpushButtonCenterClicked)



    def onpushButtonMoveCoordsClicked(self) -> None:
        """
        slot for onpushButtonMoveCoordsClicked
        :return:
        """
        self.move(QtCore.QPoint(self.ui.spinBoxX.value(), self.ui.spinBoxY.value()))

    def onpushButtonLTClicked(self) -> None:
        """
        slot for onpushButtonLTClicked
        :return:
        """
        current_pos = self.pos()
        new_pos = current_pos + QtCore.QPoint(-1, -1)
        self.move(new_pos)
    def onpushButtonLBClicked(self) -> None:
        """
        slot for onpushButtonLBClicked
        :return:
        """
        current_pos = self.pos()
        new_pos = current_pos + QtCore.QPoint(-1, 1)
        self.move(new_pos)
    def onpushButtonRTClicked(self) -> None:
        """
        slot for onpushButtonRTClicked
        :return:
        """
        current_pos = self.pos()
        new_pos = current_pos + QtCore.QPoint(1, -1)
        self.move(new_pos)
    def onpushButtonRBClicked(self) -> None:
        """
        slot for onpushButtonRBClicked
        :return:
        """
        current_pos = self.pos()
        new_pos = current_pos + QtCore.QPoint(1, 1)
        print(new_pos)
        self.move(new_pos)
    def onpushButtonCenterClicked(self) -> None:
        """
        slot for onpushButtonCenterClicked
        :return:
        """
        self.move(QtCore.QPoint(self.centerofapp[0], self.centerofapp[1]))

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        event Move
        :param event:
        :return:
        """
        print(f'{self.getTimeNow()}: new pos:{event.pos().x()},{event.pos().y()}, old pos:{event.oldPos().x()},{event.oldPos().y()}')
        self.ui.plainTextEdit.appendPlainText(
            f'{self.getTimeNow()}: Текущее положение {self.pos().x()},{self.pos().y()}')

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        event resize
        :param event:
        :return:
        """
        print(f'{self.getTimeNow()}: new size:{event}')



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
