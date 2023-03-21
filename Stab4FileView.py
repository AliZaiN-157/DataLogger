from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
import resources_rc


class Stab4FileView(QMainWindow):
    def __init__(self):
        super().__init__()
        super(Stab4FileView, self).__init__()
        uic.loadUi('Stab1.ui', self)
        self.DataPanelButton.clicked.connect(self.GotoDataPanel)
        self.HomeButton.clicked.connect(self.GotoHome)
        self.AlarmButton.clicked.connect(self.GotoAlarm)
        self.Stab1_button.clicked.connect(self.GotoStab1)
        self.Stab2_button.clicked.connect(self.GotoStab2)
        self.Stab3_button.clicked.connect(self.GotoStab3)
        self.Stab4_button.clicked.connect(self.GotoStab4)
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

if __name__ == '__main__':
    app = QApplication([])
    widget = Stab4FileView()
    widget.show()
    app.exec_()
