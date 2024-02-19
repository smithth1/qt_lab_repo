import psutil,time
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

        while self.status:
            cpu_value = psutil.cpu_percent()
            cpu_count_l = psutil.cpu_count(logical=True)
            cpu_count_p = psutil.cpu_count(logical=False)
            cpu_memo = psutil.virtual_memory()
            battery = psutil.sensors_battery()
            bat_info = battery.percent

            cpu_memo_total = cpu_memo.total
            cpu_memo_available = cpu_memo.available
            ram_value = psutil.virtual_memory().percent
            data = []
            data.append(cpu_memo_total)
            data.append(cpu_memo_available)
            data.append(cpu_value)
            data.append(cpu_count_p)
            data.append(cpu_count_l)
            data.append(ram_value)
            data.append(bat_info)
            self.systemSignal.emit(data)
            time.sleep(self.delay)


class SysProcesses(QtCore.QThread):
    ProcessSignal = QtCore.Signal(list)
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

        while self.status:
            processes = []
            for process in psutil.process_iter(['pid', 'name']):
                processes.append(process.info)
            self.ProcessSignal.emit(processes)
            time.sleep(self.delay)

class SysServices(QtCore.QThread):
    ServicesSignal = QtCore.Signal(list)
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

        while self.status:
            services = []
            data = []
            for service in psutil.win_service_iter():
                services.append(service.name())
            for srv in services:
                try:
                    data.append(psutil.win_service_get(srv).as_dict())
                except:
                    None
            self.ServicesSignal.emit(data)
            time.sleep(self.delay)