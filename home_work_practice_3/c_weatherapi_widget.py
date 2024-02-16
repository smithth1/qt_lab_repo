"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""


from PySide6 import QtWidgets, QtCore
from ui.weathermeter import Ui_Form
from a_threads import WeatherHandler

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBoxDelay.addItems(["3 sec", "5 sec", "10 sec"])
        self.ui.lineEditlat.setPlaceholderText("from -90 to 90")
        self.ui.lineEditlong.setPlaceholderText("from -180 to 180")
        self.InitSignal()

    def InitSignal(self) -> None:
        self.ui.pushButtonGetW.toggled.connect(self.onPushButtonGetWToggled)

    def onPushButtonGetWToggled(self) -> None:
        if self.validatelatlong():
            if self.ui.pushButtonGetW.isChecked():
                self.thread = WeatherHandler(self.lat, self.lon)
                self.thread.delay = self.getDelay()
                self.thread.WeatherSignal.connect(lambda data: self.info(data))
                self.ui.lineEditlat.setDisabled(True)
                self.ui.lineEditlong.setDisabled(True)
                self.ui.comboBoxDelay.setDisabled(True)
            else:
                self.thread.status = False
                self.ui.lineEditlat.setDisabled(False)
                self.ui.lineEditlong.setDisabled(False)
                self.ui.comboBoxDelay.setDisabled(False)
        else:
            self.ui.pushButtonGetW.setChecked(False)

    def getDelay(self) -> int:
        if self.ui.comboBoxDelay.currentIndex() == 0:
            return 3
        elif self.ui.comboBoxDelay.currentIndex() == 1:
            return 5
        elif self.ui.comboBoxDelay.currentIndex() == 2:
            return 10

    def validatelatlong(self):
        lattext = self.ui.lineEditlat.text()
        longtext = self.ui.lineEditlong.text()
        try:
            latfloat = float(lattext)
            longfloat = float(longtext)
            if -90 <= latfloat <= 90:
                self.ui.lineEditlat.setStyleSheet("")
                self.lat = latfloat
            else:
                self.ui.textEditWeather.setText('wrong latitude')
                return False

            if -180 <= longfloat <= 180:
                self.lon = longfloat

            else:
                self.ui.textEditWeather.setText('wrong longitude')
                return False
            return True

        except ValueError:
            self.ui.textEditWeather.setText("Введите корректные координаты")
            return False
    def info(self, data: dict):
        curweather = data['current_weather']
        curweatherunit= data['current_weather_units']
        weather = (f"date and time: {curweather['time']}\n" 
               f"temperature: {curweather['temperature']} {curweatherunit['temperature']} \n" 
               f"windspeed: {curweather['windspeed']} {curweatherunit['windspeed']} \n"
               f"winddirection: {curweather['winddirection']} {curweatherunit['winddirection']} \n")
        self.ui.textEditWeather.append(weather)




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()