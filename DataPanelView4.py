from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from datetime import datetime
import resources_rc

import database
db = database.DB()

class DataTable(QMainWindow):
    def __init__(self):
        super().__init__()
        super(DataTable, self).__init__()
        uic.loadUi('DataTable.ui', self)
        self.Back.clicked.connect(self.GotoStab4)
        self.HomeButton.clicked.connect(self.GotoHome)
        self.AlarmButton.clicked.connect(self.GotoAlarm)
        self.Stab1_button.clicked.connect(self.GotoStab1)
        self.Stab2_button.clicked.connect(self.GotoStab2)
        self.Stab3_button.clicked.connect(self.GotoStab3)
        self.Stab4_button.clicked.connect(self.GotoStab4)
        self.Search.clicked.connect(self.search)
        self.tableWidget.setColumnWidth(0, 120)
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 220)
        self.tableWidget.setColumnWidth(3, 220)
        self.show()

    def GotoDataPanel(self):
        self.close()
        from DataPanelView import DataTable
        self.window = DataTable()
        self.window.show()

    def GotoHome(self):
        self.close()
        from datalogger import MainWindow
        self.window = MainWindow()
        self.window.show()

    def GotoAlarm(self):
        self.close()
        from Alarm import Alarm
        self.window = Alarm()
        self.window.show()
    
    def GotoStab1(self):
        self.close()
        from Stab1FileView import Stab1FileView
        self.window = Stab1FileView()
        self.window.show()
    
    def GotoStab2(self):
        self.close()
        from Stab2FileView import Stab2FileView
        self.window = Stab2FileView()
        self.window.show()
    
    def GotoStab3(self):
        self.close()
        from Stab3FileView import Stab3FileView
        self.window = Stab3FileView()
        self.window.show()
    
    def GotoStab4(self):
        self.close()
        from Stab4FileView import Stab4FileView
        self.window = Stab4FileView()
        self.window.show()

    def search(self):
        print(self.from_dateTime.dateTime().toString(Qt.ISODate))
        from_date = self.from_dateTime.dateTime().date().toString(Qt.ISODate)
        from_time = self.from_dateTime.dateTime().time().toString(Qt.ISODate)
        to_date = self.to_dateTime.dateTime().date().toString(Qt.ISODate)
        to_time = self.to_dateTime.dateTime().time().toString(Qt.ISODate)

        
        # from_date = datetime.strptime(from_date, '%y/%m/%d %H:%M:%S')
        # to_date = datetime.strptime(to_date, '%y/%m/%d %H:%M:%S')
        # new_date = from_date-to_date
        # print(new_date)
        Humidity_query = """option v = {timeRangeStart: -1d, timeRangeStop: now()}
                from(bucket: "DEV")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_4")
                |> filter(fn: (r) => r["_field"] == "Humidity")
            """
        Temperature_query = """option v = {timeRangeStart: -1d, timeRangeStop: now()}
                from(bucket: "DEV")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_4")
                |> filter(fn: (r) => r["_field"] == "Temperature")
            """
        table1 = db.query(Humidity_query)
        table2 = db.query(Temperature_query)

        temp=[]
        humd=[]
        date=[]
        time=[]
        for table in table1:
            for record in table.records:
                humd.append(record.values.get('_value'))

        for table in table2:
            for record in table.records:
                date.append(record.values.get('_time').date())
                time.append(record.values.get('_time').time())
                temp.append(record.values.get('_value'))

        data=[]
        for i in range(len(date)):
            data.append({'date':date[i], "time":time[i], "temperature":temp[i], "humidity":humd[i]})
        row=0
        self.tableWidget.setRowCount(len(data))
        for i in data:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(i['date'])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(i['time'])))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(i['temperature'])))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(i['humidity'])))
            row+=1
            

            

if __name__ == '__main__':
    app = QApplication([])
    widget = DataTable()
    widget.show()
    app.exec_()
