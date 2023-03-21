from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
import resources_rc
import os

from dotenv import load_dotenv
load_dotenv()

un = os.getenv("AUTH_USERNAME")
pw = os.getenv("AUTH_PASSWORD")

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        super(Login, self).__init__()
        uic.loadUi('Login.ui', self)
        self.login.clicked.connect(self.loginUser)
        self.show()

    def loginUser(self):
        username = self.username.text()
        password = self.password.text()
        if (username == un and password == pw):
            self.close()
            from datalogger import MainWindow
            self.window = MainWindow()
            self.window.show()
            

if __name__ == '__main__':
    app = QApplication([])
    widget = Login()
    widget.show()
    app.exec_()
