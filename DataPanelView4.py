from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from datetime import datetime
import resources_rc

from create_table_fpdf2 import PDF #for pdf

import database
db = database.DB()

class DataTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.temp=[]
        self.humd=[]
        self.date=[]
        self.time=[]
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
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Humidity4")
            """
        Temperature_query = """option v = {timeRangeStart: -1d, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Temperature4")
            """
        table1 = db.query(Humidity_query)
        table2 = db.query(Temperature_query)


        for table in table1:
            for record in table.records:
                self.humd.append(str(record.values.get('_value')))

        for table in table2:
            for record in table.records:
                self.date.append(str(record.values.get('_time').date()))
                self.time.append(str(record.values.get('_time').time()))
                self.temp.append(str(record.values.get('_value')))

        data=[]
        for i in range(len(self.humd)):
            data.append({'date':self.date[i], "time":self.time[i], "temperature":self.temp[i], "humidity":self.humd[i]})
        row=0
        self.tableWidget.setRowCount(len(data))
        for i in data:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(i['date']))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(i['time']))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(i['temperature']))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(i['humidity']))
            row+=1

    def pdf_btn(self):

        data_pdf = {'Date':self.date,'Time':self.time,'Temperature':self.temp,'Humidity':self.humd}

        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Times", size=11)

        pdf.create_table(table_data = data_pdf,title='Data Logger Stability Chamber 1', cell_width='even')
        pdf.ln()

        pdf.output('STAB_4_Data/new.pdf')
            

            

if __name__ == '__main__':
    app = QApplication([])
    widget = DataTable()
    widget.show()
    app.exec_()
