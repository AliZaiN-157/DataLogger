from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic


class DataTable(QMainWindow):
    def __init__(self):
        super().__init__()
        super(DataTable, self).__init__()
        uic.loadUi('DataTable.ui', self)
        self.Search.clicked.connect(self.search)
        self.tableWidget.setColumnWidth(0, 120)
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 220)
        self.tableWidget.setColumnWidth(3, 220)
        self.show()

    def search(self):
        print(self.from_dateTime.dateTime().toString(Qt.ISODate))
        from_date = self.from_dateTime.dateTime().date().toString(Qt.ISODate)
        from_time = self.from_dateTime.dateTime().time().toString(Qt.ISODate)
        to_date = self.to_dateTime.dateTime().date().toString(Qt.ISODate)
        to_time = self.to_dateTime.dateTime().time().toString(Qt.ISODate)
        Humidity_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "DEV")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Humidity")
            """
        data=[{'date:':'date','time':'time','tempearature':20,'humidity':30},{'date:':'date:','time':'time','tempearature':20,'humidity':30}]
        self.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(data[i])['date'])
            self.tableWidget.setItem(i, 1, QTableWidgetItem(data[i])['time'])
            self.tableWidget.setItem(i, 2, QTableWidgetItem(data[i]['tempearature']))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(data[i]['humidity']))
            

if __name__ == '__main__':
    app = QApplication([])
    widget = DataTable()
    widget.show()
    app.exec_()
