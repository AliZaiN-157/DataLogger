from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
# import resources_rc

# import database
# db = database.DB()

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        super(Login, self).__init__()
        uic.loadUi('Login.ui', self)
       
        self.show()

            

if __name__ == '__main__':
    app = QApplication([])
    widget = Login()
    widget.show()
    app.exec_()
