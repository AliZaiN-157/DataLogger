from PyQt5.QtWidgets import QFileSystemModel
from PyQt5.QtCore import QTimer, Qt, QModelIndex,QDir
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTreeWidget
from PyQt5 import uic
from PyQt5 import QtGui
import resources_rc
import os

def populate_tree_widget(parent_item, path):
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                # If the item is a directory, create a new parent item and populate it recursively
                dir_item = QTreeWidgetItem(parent_item, [item, 'Directory', '', ''])
                populate_tree_widget(dir_item, full_path)
            else:
                # If the item is a file, create a new child item and set its data
                size = os.path.getsize(full_path)
                date_modified = os.path.getmtime(full_path)
                file_item = QTreeWidgetItem(parent_item, [item, 'File', str(size), str(date_modified)])

class Stab1FileView(QMainWindow):
    def __init__(self, dir_path):
        super().__init__()
        super(Stab1FileView, self).__init__()
        uic.loadUi('Stab1.ui', self)
        self.HomeButton.clicked.connect(self.GotoHome)
        self.AlarmButton.clicked.connect(self.GotoAlarm)
        self.DataPanelButton.clicked.connect(self.GotoDataPanel)
        self.Stab1_button.clicked.connect(self.GotoStab1)
        self.Stab2_button.clicked.connect(self.GotoStab2)
        self.Stab3_button.clicked.connect(self.GotoStab3)
        self.Stab4_button.clicked.connect(self.GotoStab4)
        self.LogoutButton.clicked.connect(self.Logout)
       
        self.tree.setHeaderLabels(['Name', 'Type', 'Size', 'Date Modified'])
        self.tree.setColumnWidth(0, 250)
        self.tree.setColumnWidth(1, 100)
        self.tree.setColumnWidth(2, 100)
        self.tree.setColumnWidth(3, 150)
        # Click on file to open
        self.tree.itemDoubleClicked.connect(lambda item, column: self.open_file(item, column, dir_path))
        populate_tree_widget(self.tree, dir_path)
        self.show()

    def open_file(self, item, column, dir_path):
        if item.childCount() == 0:
            os.startfile(os.path.join(dir_path, '', '') + item.text(0))

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
    
    def Logout(self):
        self.close()
        from Login import Login
        self.window = Login()
        self.window.show()

    
if __name__ == '__main__':
    app = QApplication([])
    dirPath = r'D:\Ahsan\DataLogger-1\STAB_1_Data'
    widget = Stab1FileView(dirPath)
    widget.show()
    app.exec_()
