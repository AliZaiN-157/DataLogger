from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import resources_rc


import database
db = database.DB()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('datalogger.ui', self)

        self.show()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(5000)

    def update_data(self):
        Humidity_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Humidity")
            """
        Temperature_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Temperature")
            """
        Humidity_setpoint_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "HUM_Setpoint")

            """
        Temperature_setpoint_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "TEMP_Setpoint")
            """
        humidity_stab1 = db.query(Humidity_query)
        for table in humidity_stab1:
            for record in table.records:
                self.Stab1_Humd_4.setValue(record.values.get('_value'))
                self.stab1_humd.setText(str(record.values.get('_value')))
        temperature_stab1 = db.query(Temperature_query)
        for table in temperature_stab1:
            for record in table.records:
                self.Stab1_Temp_4.setValue(record.values.get('_value'))
                self.stab1_temp.setText(str(record.values.get('_value')))
        humidity_setpoint_stab1 = db.query(Humidity_setpoint_query)
        for table in humidity_setpoint_stab1:
            for record in table.records:
                self.max_hum_1.setText(str(record.values.get('_value')+5))
                self.min_hum_1.setText(str(record.values.get('_value')-5))
        temperature_setpoint_stab1 = db.query(Temperature_setpoint_query)
        for table in temperature_setpoint_stab1:
            for record in table.records:
                self.max_tmp_1.setText(str(record.values.get('_value')+5))
                self.min_tmp_1.setText(str(record.values.get('_value')-5))

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
        date = self.from_dateTime.dateTime().date().toString(Qt.ISODate)
        time = self.from_dateTime.dateTime().time().toString(Qt.ISODate)
        data=[{'date:':date,'time':time,'tempearature':20,'humidity':30},{'date:':date,'time':time,'tempearature':20,'humidity':30}]
        self.tableWidget.setRowCount(len(date))
        for i in range(len(date)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(date[i]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(time[i]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(data[i]['tempearature']))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(data[i]['humidity']))

def main():
    app = QApplication([])
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(MainWindow())
    widget.addWidget(DataTable())
    window = MainWindow()
    app.exec_()



if __name__ == '__main__':
    main()

