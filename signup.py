import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from signup_ui import Ui_Dialog
import pymongo
from main import widget
from validations import is_valid_password, is_valid_email
import login
from mydatabase import collection

# Sets up the UI, connects button clicks to their respective functions
class SignupDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signup_button.clicked.connect(self.signup)
        self.uname_line.textChanged.connect(self.check_username)
        self.signup_button_3.clicked.connect(self.open_login)
        self.password_lineEdit.textChanged.connect(self.check_password)
        self.login_dialog = None

    # Checks if username is alphanumeric and sets the buttons and the value of the username
    def check_username(self):
        username = self.uname_line.text()
        if not username.isalnum():
            self.uname_line.setStyleSheet("background-color: #FFB6C1")
            self.signup_button.setEnabled(False)
        else:
            self.uname_line.setStyleSheet("")
            self.signup_button.setEnabled(True)

    # Checks if password is valid and sets the buttons and the value of the password
    def check_password(self):
        password = self.password_lineEdit.text()
        if not is_valid_password(password):
            self.password_lineEdit.setStyleSheet("background-color: #FFB6C1")
            self.signup_button.setEnabled(False)
        else:
            self.password_lineEdit.setStyleSheet("")
            self.signup_button.setEnabled(True)

    # Handles signup conditions to add to the database
    def signup(self):
        username = self.uname_line.text()
        email = self.email_lineEdit.text()
        password = self.password_lineEdit.text()
        query = {"$or": [{"username": username}, {"email": email}]}
        result = collection.find_one(query)
        if result:
            QMessageBox.warning(self, "Signup Error", "Username or email already exists")
        elif not is_valid_email(email):
            QMessageBox.warning(self, "Signup Error", "Invalid email address")
        else:
            new_user = {
                "username": username,
                "email": email,
                "password": password
            }
            collection.insert_one(new_user)
            QMessageBox.information(self, "Signup Success", "User successfully registered")
            self.open_login()

    # Opens the login widget
    def open_login(self):
        self.login_dialog = login.LoginDialog()
        widget.addWidget(self.login_dialog)
        widget.setCurrentIndex(widget.currentIndex() + 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = SignupDialog()
    dialog.show()
    sys.exit(app.exec_())
