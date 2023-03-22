from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
import resources_rc


class Alarm(QMainWindow):
    def __init__(self):
        super().__init__()
        super(Alarm, self).__init__()
        uic.loadUi('alarmpage.ui', self)
        self.HomeButton.clicked.connect(self.GotoHome)
        self.AlarmButton.clicked.connect(self.GotoAlarm)
        self.Stab1_button.clicked.connect(self.GotoStab1)
        self.Stab2_button.clicked.connect(self.GotoStab2)
        self.Stab3_button.clicked.connect(self.GotoStab3)
        self.Stab4_button.clicked.connect(self.GotoStab4)
        self.LogoutButton.clicked.connect(self.Logout)

        # read alert.txt and show in table
        

        self.AlarmTable.setColumnWidth(0, 80)
        self.AlarmTable.setColumnWidth(1, 150)
        self.AlarmTable.setColumnWidth(2, 180)
        self.AlarmTable.setColumnWidth(3, 30)
        
       
        self.show()
        # read data from alert.txt and show in table
        self.data = []
        with open('alert.txt', 'r') as f:
            for line in f:
                self.data.append({
                    'device': line.split(' ')[0],
                    'alarm': line.split(' ')[1],
                    'time': line.split(' ')[2]
                })
        row=0
        self.AlarmTable.setRowCount(len(self.data))
        for i in self.data:
            self.AlarmTable.setItem(row, 0, QTableWidgetItem(i['device']))
            self.AlarmTable.setItem(row, 1, QTableWidgetItem(i['alarm']))
            self.AlarmTable.setItem(row, 2, QTableWidgetItem(i['time']))
            button = QPushButton()
            button.setIcon(QtGui.QIcon(':/icons/icons/trash-2.svg'))
            # button.setIconSize(QtGui.QSize(20, 20))
            # button.clicked.connect(self.view)
            self.AlarmTable.setCellWidget(row, 3, button)
            row+=1
    
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
    
    def Logout(self):
        self.close()
        from Login import Login
        self.window = Login()
        self.window.show()
            

if __name__ == '__main__':
    app = QApplication([])
    widget = Alarm()
    widget.show()
    app.exec_()
