from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets , QtGui
from PyQt5.QtCore import *
import resources_rc

from Alarm import Alarm
alert = Alarm()

from database import DB
db = DB()




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('datalogger.ui', self)
        self.AlarmButton.clicked.connect(self.GotoAlarm)
        self.Stab1_button.clicked.connect(self.GotoStab1)
        self.Stab2_button.clicked.connect(self.GotoStab2)
        self.Stab3_button.clicked.connect(self.GotoStab3)
        self.Stab4_button.clicked.connect(self.GotoStab4)
        self.LogoutButton.clicked.connect(self.Logout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(5000)
        self.Stab1_Humd_4.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: #35a811;"
                        "}")
        self.Stab1_Temp_4.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: #35a811;"
                        "}")

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
    
    def Logout(self):
        self.close()
        from Login import Login
        self.window = Login()
        self.window.show()

    def update_data(self):
        Humidity_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "DEV")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Humidity")
            """
        Temperature_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "DEV")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Temperature")
            """
        Humidity_setpoint_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "DEV")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "HUM_Setpoint")

            """
        Temperature_setpoint_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "DEV")
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
                if (self.Stab1_Humd_4.value() > record.values.get('_value')+5):
                    self.Stab1_Humd_4.setStyleSheet("QProgressBar::chunk "
                            "{"
                                "background-color: red;"
                            "}")
                    alert.call_Alert(1,"STAB_1","High Humidity", record.values.get('_time').time())
                elif (self.Stab1_Humd_4.value() < record.values.get('_value')-5):
                    self.Stab1_Humd_4.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: yellow;"
                        "}")
                    alert.call_Alert(1,"STAB_1","Low Humidity", record.values.get('_time').time())
                else:
                    self.Stab1_Humd_4.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: #35a811;"
                        "}")
                self.max_hum_1.setText(str(record.values.get('_value')+5))
                self.min_hum_1.setText(str(record.values.get('_value')-5))
        temperature_setpoint_stab1 = db.query(Temperature_setpoint_query)
        for table in temperature_setpoint_stab1:
            for record in table.records: 
                if (self.Stab1_Temp_4.value() > record.values.get('_value')+2):
                    self.Stab1_Temp_4.setStyleSheet("QProgressBar::chunk "
                            "{"
                                "background-color: red;"
                            "}")
                    alert.call_Alert(1,"STAB_1","High Temperature", record.values.get('_time').time())
                elif (self.Stab1_Temp_4.value() < record.values.get('_value')-2):
                    self.Stab1_Temp_4.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: yellow;"
                        "}")
                    alert.call_Alert(1,"STAB_1","Low Temperature", record.values.get('_time').time())
                else:
                    self.Stab1_Temp_4.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: #35a811;"
                        "}")
                self.max_tmp_1.setText(str(record.values.get('_value')+2))
                self.min_tmp_1.setText(str(record.values.get('_value')-2))



def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()

