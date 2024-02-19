from PySide6 import QtWidgets,QtGui
from ui.sysinfo_main import Ui_Form
from workers import SystemInfo, SysProcesses, SysServices
import psutil,platform,wmi,pythoncom



class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.disks = wmi.WMI().Win32_LogicalDisk()
        self.resometer_thread = SystemInfo()
        self.resometer_thread.delay = self.ui.spinBoxDelay.value()
        self.SysProcess_thread = SysProcesses()
        self.SysProcess_thread.delay = self.ui.spinBoxDelay.value()
        self.SysService_thread = SysServices()
        self.SysService_thread.delay = self.ui.spinBoxDelay.value()
        self.InitSignal()
        self.InitUi()

    def InitUi(self):
        pythoncom.CoInitialize()
        self.ui.textEditSysInfo.setPlainText(
            f'CurrentUser: {psutil.users()[0].name:>15}\n'
            f'OS:          {platform.system():>15}\n'
            f'OS Version:  {platform.version():>15}\n'
            f'OS Release:  {platform.release():>15}\n'
            f'OS Bit:      {platform.architecture()[0]:>15}\n\n'
            f'Discs: \n'
        )
        self.ui.textEditSysInfo.append(self.diskinfo())

    def diskinfo(self):
        text = ""
        for disk in self.disks:
            text +=   (f"Label      - {disk.VolumeName:>15}\n" \
            f"Serial      - {disk.VolumeSerialNumber:>15}\n" \
            f"Type        - {disk.Description:>15}\n" \
            f"SystemName  - {disk.DeviceID:>15}\n" \
            f"FS          - {disk.FileSystem:>15}\n" \
            f"Available   - {self.format(int(disk.FreeSpace)):>15}Gb\n\n")
        return text
    def InitSignal(self) -> None:
        self.ui.spinBoxDelay.valueChanged.connect(self.delay_time_changed)
        self.resometer_thread.systemSignal.connect(lambda sysdata: self.sysinfo(sysdata))
        self.SysProcess_thread.ProcessSignal.connect(lambda procdata: self.proc(procdata))
        self.SysService_thread.ServicesSignal.connect(lambda servdata: self.serv(servdata))

    def format(self,n):
        pref = 0
        for i in range(3):
            if n > 1024:
                n = n / 1024
        return (n)
    def sysinfo(self,data):
        # print(data)
        self.ui.lcdNumberRAMA.display(int(self.format(data[0])))
        self.ui.lcdNumberRAMAV.display(int(self.format(data[1])))
        self.ui.lcdNumberRAMU.display(data[5])
        self.ui.lcdNumberCPU.display(data[2])
        self.ui.lcdNumberCPUCORES.display(data[3])
        self.ui.lcdNumberCPUTHREADS.display(data[4])
        self.ui.progressBarBattery.setValue(data[6])

    def proc(self,data):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setHorizontalHeaderLabels(['Name','Pid'])

        for rownum,row in enumerate(data):
            for columnnum,column in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(row[column]))
                self.ui.tableWidget.setItem(rownum,columnnum,item)
        self.ui.tableWidget.resizeColumnsToContents()

        # print(data)

    def serv(self,data):
        self.ui.tableWidgetServices.clear()
        self.ui.tableWidgetServices.setRowCount(len(data))
        self.ui.tableWidgetServices.setColumnCount(3)
        self.ui.tableWidgetServices.setHorizontalHeaderLabels(['Name','Start_Type','Status'])

        for rownum,row in enumerate(data):
            for column in row:
                item1 = QtWidgets.QTableWidgetItem(str(row['display_name']))
                item2 = QtWidgets.QTableWidgetItem(str(row['start_type']))
                item3 = QtWidgets.QTableWidgetItem(str(row['status']))
                self.ui.tableWidgetServices.setItem(rownum,0,item1)
                self.ui.tableWidgetServices.setItem(rownum, 1, item2)
                self.ui.tableWidgetServices.setItem(rownum, 2, item3)


    def delay_time_changed(self):
        self.resometer_thread.delay = self.ui.spinBoxDelay.value()
        self.SysProcess_thread.delay = self.ui.spinBoxDelay.value()
        self.SysService_thread.delay = self.ui.spinBoxDelay.value()

        if self.SysService_thread.isRunning() == False:
            self.SysService_thread.start()
        if self.SysProcess_thread.isRunning() == False:
            self.SysProcess_thread.start()
        if self.resometer_thread.isRunning() == False:
            self.resometer_thread.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()