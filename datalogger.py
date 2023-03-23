from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets , QtGui
from PyQt5.QtCore import *
import resources_rc

from Alarm import Alarm
alert = Alarm

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
        # self.Stab1_Humd_4.setStyleSheet("QProgressBar::chunk "
        #                 "{"
        #                     "background-color: #35a811;"
        #                 "}")
        # self.Stab1_Temp_4.setStyleSheet("QProgressBar::chunk "
        #                 "{"
        #                     "background-color: #35a811;"
        #                 "}")
        # self.Stab1_Humd_7.setStyleSheet("QProgressBar::chunk "
        #                 "{"
        #                     "background-color: #35a811;"
        #                 "}")
        # self.Stab1_Temp_7.setStyleSheet("QProgressBar::chunk "
        #                 "{"
        #                     "background-color: #35a811;"
        #                 "}")

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
        Humidity1_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Humidity")
                |> last()
            """
        Temperature1_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Temperature1")
                |> last()
            """
        Humidity1_setpoint_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "HUM_Setpoint1")
                |> last()
            """
        Temperature1_setpoint_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "TEMP_Setpoint1")
                |> last()
            """
        Humidity2_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Humidity2")
                |> last()
            """
        Temperature2_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Temperature2")
                |> last()
            """
        Humidity2_setpoint_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "HUM_Setpoint2")
                |> last()

            """
        Temperature2_setpoint_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "TEMP_Setpoint2")
                |> last()
            """
        Humidity3_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Humidity3")
                |> last()
            """
        Temperature3_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Temperature3")
                |> last()
            """
        Humidity3_setpoint_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "HUM_Setpoint3")
                |> last()

            """
        Temperature3_setpoint_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "TEMP_Setpoint3")
                |> last()
            """
        Humidity4_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Humidity4")
                |> last()
            """
        Temperature4_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Temperature4")
                |> last()
            """
        Humidity4_setpoint_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "HUM_Setpoint4")
                |> last()

            """
        Temperature4_setpoint_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "TEST")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "TEMP_Setpoint4")
                |> last()
            """

        """CHAMBER 1 DATA"""

        humidity_stab1 = db.query(Humidity1_query)
        for table in humidity_stab1:
            for record in table.records:
                self.Stab1_Humd_4.setValue(record.values.get('_value'))
                self.stab1_humd.setText(str(record.values.get('_value')))
        temperature_stab1 = db.query(Temperature1_query)
        for table in temperature_stab1:
            for record in table.records:
                self.Stab1_Temp_4.setValue(record.values.get('_value'))
                self.stab1_temp.setText(str(record.values.get('_value')))
        humidity_setpoint_stab1 = db.query(Humidity1_setpoint_query)
        for table in humidity_setpoint_stab1:
            for record in table.records:
                if (self.Stab1_Humd_4.value() > record.values.get('_value')+5):
                    self.Stab1_Humd_4.setStyleSheet("QProgressBar::chunk "
                            "{"
                                "background-color: red;"
                            "}")
                    alert.call_Alert(1,"STAB_1","High Humidity", str(record.values.get('_time').time()))
                elif (self.Stab1_Humd_4.value() < record.values.get('_value')-5):
                    self.Stab1_Humd_4.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: yellow;"
                        "}")
                    alert.call_Alert(1,"STAB_1","Low Humidity",str(record.values.get('_time').time()))
                else:
                    self.Stab1_Humd_4.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: #35a811;"
                        "}")
                self.max_hum_1.setText(str(record.values.get('_value')+5))
                self.min_hum_1.setText(str(record.values.get('_value')-5))
        temperature_setpoint_stab1 = db.query(Temperature1_setpoint_query)
        for table in temperature_setpoint_stab1:
            for record in table.records: 
                if (self.Stab1_Temp_4.value() > record.values.get('_value')+2):
                    self.Stab1_Temp_4.setStyleSheet("QProgressBar::chunk "
                            "{"
                                "background-color: red;"
                            "}")
                    alert.call_Alert(1,"STAB_1","High Temperature",str(record.values.get('_time').time()))
                elif (self.Stab1_Temp_4.value() < record.values.get('_value')-2):
                    self.Stab1_Temp_4.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: yellow;"
                        "}")
                    alert.call_Alert(1,"STAB_1","Low Temperature",str(record.values.get('_time').time()))
                else:
                    self.Stab1_Temp_4.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: #35a811;"
                        "}")
                self.max_tmp_1.setText(str(record.values.get('_value')+2))
                self.min_tmp_1.setText(str(record.values.get('_value')-2))

            """CHAMBER 2 DATA"""

        humidity_stab2 = db.query(Humidity2_query)
        for table in humidity_stab2:
            for record in table.records:
                self.Stab1_Humd_7.setValue(record.values.get('_value'))
                self.stab1_temp_8.setText(str(record.values.get('_value')))
        temperature_stab2 = db.query(Temperature2_query)
        for table in temperature_stab2:
            for record in table.records:
                self.Stab1_Temp_7.setValue(record.values.get('_value'))
                self.stab1_temp_4.setText(str(record.values.get('_value')))
        humidity_setpoint_stab2 = db.query(Humidity2_setpoint_query)
        for table in humidity_setpoint_stab2:
            for record in table.records:
                if (self.Stab1_Humd_7.value() > record.values.get('_value')+5):
                    self.Stab1_Humd_7.setStyleSheet("QProgressBar::chunk "
                            "{"
                                "background-color: red;"
                            "}")
                    alert.call_Alert(1,"STAB_2","High Humidity",str(record.values.get('_time').time()))
                elif (self.Stab1_Humd_7.value() < record.values.get('_value')-5):
                    self.Stab1_Humd_7.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: yellow;"
                        "}")
                    alert.call_Alert(1,"STAB_2","Low Humidity",str(record.values.get('_time').time()))
                else:
                    self.Stab1_Humd_7.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: #35a811;"
                        "}")
                self.max_hum_2.setText(str(record.values.get('_value')+5))
                self.min_hum_2.setText(str(record.values.get('_value')-5))
        temperature_setpoint_stab2 = db.query(Temperature2_setpoint_query)
        for table in temperature_setpoint_stab2:
            for record in table.records: 
                if (self.Stab1_Temp_7.value() > record.values.get('_value')+2):
                    self.Stab1_Temp_7.setStyleSheet("QProgressBar::chunk "
                            "{"
                                "background-color: red;"
                            "}")
                    alert.call_Alert(1,"STAB_2","High Temperature",str(record.values.get('_time').time()))
                elif (self.Stab1_Temp_7.value() < record.values.get('_value')-2):
                    self.Stab1_Temp_7.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: yellow;"
                        "}")
                    alert.call_Alert(1,"STAB_2","Low Temperature",str(record.values.get('_time').time()))
                else:
                    self.Stab1_Temp_7.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: #35a811;"
                        "}")
                self.max_tmp_2.setText(str(record.values.get('_value')+2))
                self.min_tmp_2.setText(str(record.values.get('_value')-2))

                """CHAMBER 3 DATA"""

        humidity_stab3 = db.query(Humidity3_query)
        for table in humidity_stab3:
            for record in table.records:
                self.Stab1_Humd_8.setValue(record.values.get('_value'))
                self.stab1_temp_10.setText(str(record.values.get('_value')))
        temperature_stab3 = db.query(Temperature3_query)
        for table in temperature_stab3:
            for record in table.records:
                self.Stab1_Temp_8.setValue(record.values.get('_value'))
                self.stab1_temp_9.setText(str(record.values.get('_value')))
        humidity_setpoint_stab3 = db.query(Humidity3_setpoint_query)
        for table in humidity_setpoint_stab3:
            for record in table.records:
                if (self.Stab1_Humd_8.value() > record.values.get('_value')+5):
                    self.Stab1_Humd_8.setStyleSheet("QProgressBar::chunk "
                            "{"
                                "background-color: red;"
                            "}")
                    alert.call_Alert(1,"STAB_3","High Humidity",str(record.values.get('_time').time()))
                elif (self.Stab1_Humd_8.value() < record.values.get('_value')-5):
                    self.Stab1_Humd_8.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: yellow;"
                        "}")
                    alert.call_Alert(1,"STAB_3","Low Humidity",str(record.values.get('_time').time()))
                else:
                    self.Stab1_Humd_8.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: #35a811;"
                        "}")
                self.max_hum_3.setText(str(record.values.get('_value')+5))
                self.min_hum_3.setText(str(record.values.get('_value')-5))
        temperature_setpoint_stab3 = db.query(Temperature3_setpoint_query)
        for table in temperature_setpoint_stab3:
            for record in table.records: 
                if (self.Stab1_Temp_8.value() > record.values.get('_value')+2):
                    self.Stab1_Temp_8.setStyleSheet("QProgressBar::chunk "
                            "{"
                                "background-color: red;"
                            "}")
                    alert.call_Alert(1,"STAB_3","High Temperature",str(record.values.get('_time').time()))
                elif (self.Stab1_Temp_8.value() < record.values.get('_value')-2):
                    self.Stab1_Temp_8.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: yellow;"
                        "}")
                    alert.call_Alert(1,"STAB_3","Low Temperature",str(record.values.get('_time').time()))
                else:
                    self.Stab1_Temp_8.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: #35a811;"
                        "}")
                self.max_tmp_3.setText(str(record.values.get('_value')+2))
                self.min_tmp_7.setText(str(record.values.get('_value')-2))

                """CHAMBER 4 DATA"""

        humidity_stab4 = db.query(Humidity4_query)
        for table in humidity_stab4:
            for record in table.records:
                self.Stab1_Humd_10.setValue(record.values.get('_value'))
                self.stab1_temp_14.setText(str(record.values.get('_value')))
        temperature_stab4 = db.query(Temperature4_query)
        for table in temperature_stab4:
            for record in table.records:
                self.Stab1_Temp_10.setValue(record.values.get('_value'))
                self.stab1_temp_13.setText(str(record.values.get('_value')))
        humidity_setpoint_stab4 = db.query(Humidity4_setpoint_query)
        for table in humidity_setpoint_stab4:
            for record in table.records:
                if (self.Stab1_Humd_10.value() > record.values.get('_value')+5):
                    self.Stab1_Humd_10.setStyleSheet("QProgressBar::chunk "
                            "{"
                                "background-color: red;"
                            "}")
                    alert.call_Alert(1,"STAB_4","High Humidity",str(record.values.get('_time').time()))
                elif (self.Stab1_Humd_10.value() < record.values.get('_value')-5):
                    self.Stab1_Humd_10.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: yellow;"
                        "}")
                    alert.call_Alert(1,"STAB_4","Low Humidity",str(record.values.get('_time').time()))
                else:
                    self.Stab1_Humd_10.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: #35a811;"
                        "}")
                self.max_hum_4.setText(str(record.values.get('_value')+5))
                self.min_hum_4.setText(str(record.values.get('_value')-5))
        temperature_setpoint_stab4 = db.query(Temperature4_setpoint_query)
        for table in temperature_setpoint_stab4:
            for record in table.records: 
                if (self.Stab1_Temp_10.value() > record.values.get('_value')+2):
                    self.Stab1_Temp_10.setStyleSheet("QProgressBar::chunk "
                            "{"
                                "background-color: red;"
                            "}")
                    alert.call_Alert(1,"STAB_4","High Temperature",str(record.values.get('_time').time()))
                elif (self.Stab1_Temp_10.value() < record.values.get('_value')-2):
                    self.Stab1_Temp_10.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: yellow;"
                        "}")
                    alert.call_Alert(1,"STAB_4","Low Temperature",str(record.values.get('_time').time()))
                else:
                    self.Stab1_Temp_10.setStyleSheet("QProgressBar::chunk "
                        "{"
                            "background-color: #35a811;"
                        "}")
                self.max_tmp_4.setText(str(record.values.get('_value')+2))
                self.min_tmp_8.setText(str(record.values.get('_value')-2))



def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()

