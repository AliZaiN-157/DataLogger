from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui
import resources_rc

# import database
# db = database.DB()

class Alarm(QMainWindow):
    def __init__(self):
        super().__init__()
        super(Alarm, self).__init__()
        uic.loadUi('alarmpage.ui', self)
        self.AlarmTable.setColumnWidth(0, 30)
        self.AlarmTable.setColumnWidth(1, 100)
        self.AlarmTable.setColumnWidth(2, 150)
        self.AlarmTable.setColumnWidth(3, 150)
        self.AlarmTable.setColumnWidth(4, 30)
       
        self.show()

        data=[{"id":1,"device":"Stab_1","alarm":"High Temperature","time":"2020-01-01 12:00:00"}]
        row=0
        self.AlarmTable.setRowCount(len(data))
        for i in data:
            self.AlarmTable.setItem(row, 0, QTableWidgetItem(str(i['id'])))
            self.AlarmTable.setItem(row, 1, QTableWidgetItem(i['device']))
            self.AlarmTable.setItem(row, 2, QTableWidgetItem(i['alarm']))
            self.AlarmTable.setItem(row, 3, QTableWidgetItem(i['time']))
            button = QPushButton()
            button.setIcon(QtGui.QIcon(':/icons/icons/trash-2.svg'))
            # button.setIconSize(QtGui.QSize(20, 20))
            # button.clicked.connect(self.view)
            self.AlarmTable.setCellWidget(row, 4, button)
            row+=1

            

if __name__ == '__main__':
    app = QApplication([])
    widget = Alarm()
    widget.show()
    app.exec_()
