"""
Модуль в котором содержатся потоки Qt
"""

import time
import psutil
import requests
from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemSignal = QtCore.Signal(list)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None
        self.status = True
        self.start()

    def setDelay(self, delay) -> None:
        self.delay = delay
        print(delay)


    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while True:
            cpu_value = psutil.cpu_percent()
            ram_value = psutil.virtual_memory().percent
            self.systemSignal.emit([cpu_value, ram_value])
            time.sleep(self.delay)



class WeatherHandler(QtCore.QThread):
    WeatherSignal = QtCore.Signal(dict)
    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)
        self.lat = lat
        self.lon = lon
        self.api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.delay = None
        self.status = True
        self.start()

    def setDelay(self, delay) -> None:
        self.delay = delay

    def setLat(self, lat) -> None:
        self.lat = lat

    def setLon(self, lon) -> None:
        self.lon = lon


    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while self.status == True:
            response = requests.get(self.api_url)
            data = response.json()
            self.WeatherSignal.emit(data)
            time.sleep(self.delay)




