from PyQt5 import QtCore, QtGui, QtWidgets
from database_connection import *
import icon_rc
import SharedPreferences
from PyQt5.QtWidgets import *
import sys
from UI_admin_login import Ui_LoginWindow
from admin_panel import *
import forgot_password


class LoginWindow(QMainWindow):

    # UI Initialization

    def __init__(self, parent=None):
        try:
            QMainWindow.__init__(self)
            self.ui = Ui_LoginWindow()
            self.ui.setupUi(self)
            self.show()
            self.checkIfUserIsAlreadyLogin()
            self.ui.error_label.setHidden(True)
            self.ui.forget_pass_btn.clicked.connect(self.showForgotPasswordPanel)
            self.ui.login_btn.clicked.connect(self.validateInput)

        except Exception as error:
            print(error)

    # check if user is already logged in

    def checkIfUserIsAlreadyLogin(self):
        fetch_login_info = open("save_login_info.txt", "r")
        Lines = fetch_login_info.readlines()
        count = 0
        for line in Lines:
            count += 1
            if count == 1:
                self.emailInput = line.strip()
                SharedPreferences.email = self.emailInput
            if count == 2:
                self.passwordInput = line.strip()
                SharedPreferences.admin_password = self.passwordInput

        fetch_login_info.close()
        self.Login()

    # show forget password panel

    def showForgotPasswordPanel(self):
        try:
            self.forgot_ui = forgot_password.ForgotPasswordWindow()
        except Exception as error:
            print(error)

    # display error message in cas of invalid email password

    def displayErrorMessage(self):
        try:
            self.ui.error_label.setHidden(False)
            self.ui.error_label.setText("Invalid Email or Password")
        except Exception as error:
            print(error)

    # display success message on login

    def displaySuccessMessage(self):
        try:
            self.ui.error_label.setHidden(False)
            self.ui.error_label.setText("Successful Login")
            self.ui.error_label.setStyleSheet("color: white;")
            self.ui.email_lineEdit.setText("")
            self.ui.password_line_edit.setText("")

        except Exception as error:
            print(error)

    # input validation

    def validateInput(self):
        try:
            self.emailInput = str(self.ui.email_lineEdit.text())
            self.passwordInput = str(self.ui.password_line_edit.text())

            if self.emailInput == "" or self.passwordInput == "":
                self.displayErrorMessage()
            else:
                self.Login()

        except Exception as error:
            print(error)

    # show de active error message if admin account is de-active

    def displayDeactiveError(self):
        try:
            self.ui.error_label.setHidden(False)
            self.ui.error_label.setText("Your account is De-active. Please Contact admin to activate your account")
        except Exception as error:
            print(error)

    # proceed to login

    def Login(self):
        try:
            self.admin_status = "Active"
            conn = createConnection()
            if conn is not None:
                connection = conn.cursor()
                connection.execute(
                    "SELECT admin_id, admin_full_name, admin_email, admin_status, admin_password FROM "
                    "RAASIET_QuizApp.dbo.tbl_admin where "
                    "admin_email = ? and admin_password  = ?",
                    (self.emailInput, self.passwordInput))
                data = connection.fetchone()
                conn.commit()
                if data is not None:
                    if data.admin_status == "de-active":
                        self.displayDeactiveError()
                    else:
                        SharedPreferences.user_name = data.admin_full_name
                        SharedPreferences.email = data.admin_email
                        SharedPreferences.admin_id = data.admin_id
                        SharedPreferences.admin_password = data.admin_password
                        self.displaySuccessMessage()
                        self.showPanel()
                else:
                    self.displayErrorMessage()

        except Exception as error:
            print(error)

    # show admin panel on successful login

    def showPanel(self):
        try:
            self._AdminPanelWindow = QtWidgets.QMainWindow()
            self.ui_admin_panel = AdminPanelWindow()
            self.close()

        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())
