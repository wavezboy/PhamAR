import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic
from login_ui import Ui_Dialog
import pymongo
from main import widget
import user_data
import start
from mydatabase import collection
import signup



# Sets up the UI, connects button clicks to their respective functions
class LoginDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.login)
        self.signu_btn.clicked.connect(self.open_signup)
        self.signup_dialog = None
        self.loginScreen = None

    # Opens the start widget of the application
    def open_start(self):
        self.start_dialog = start.StartDialog()
        widget.addWidget(self.start_dialog)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # Manages log in data
    def login(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        query = {"username": username, "password": password}
        result = collection.find_one(query)

        if result:
            QMessageBox.information(self, "Login Success", "Login successful!")
            user_data.name = username
            self.open_start()
        else:
            QMessageBox.warning(self, "Login Error", "Invalid username or password")
            self.loginScreen = LoginDialog()
            widget.addWidget(self.loginScreen)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    # Opens the signup widget of the application
    def open_signup(self):
        self.signup_dialog = signup.SignupDialog()
        widget.addWidget(self.signup_dialog)
        widget.setCurrentIndex(widget.currentIndex() + 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = LoginDialog()
    dialog.show()
    sys.exit(app.exec_())
