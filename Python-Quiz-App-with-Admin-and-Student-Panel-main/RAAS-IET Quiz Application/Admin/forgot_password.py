from PyQt5 import QtGui
from database_connection import *
from PyQt5.QtWidgets import *
import sys
from UI_forgot_password import Ui_ForgotPasswordWindow


class ForgotPasswordWindow(QMainWindow):

    # UI Initialization

    def __init__(self):
        try:
            QMainWindow.__init__(self, parent=None)
            self.ui = Ui_ForgotPasswordWindow()
            self.ui.setupUi(self)
            self.show()
            self.emailInput = str(self.ui.email_lineEdit.text())
            self.passwordInput = str(self.ui.password_line_edit.text())
            self.msgBox = QMessageBox()
            self.HideError()
            self.btnClicked()

        except Exception as error:
            print(error)

    # btn clicked to relevant functions

    def btnClicked(self):
        try:
            self.ui.change_password_btn.clicked.connect(self.validateInput)
        except Exception as error:
            print(error)

    # input validation

    def validateInput(self):
        try:
            if self.emailInput == "" or self.passwordInput == "":
                self.displayErrorMessage()
            elif len(self.passwordInput) != 8:
                self.displayPasswordErrorMessage()
            else:
                conn = createConnection()
                if conn is not None:
                    connection = conn.cursor()
                    connection.execute("SELECT admin_email FROM RAASIET_QuizApp.dbo.tbl_admin where admin_email = ?",
                                       self.emailInput)
                    data = connection.fetchone()
                    conn.commit()
                    if data.admin_email == self.emailInput:
                        self.HideError()
                        self.ChangePassword()
                    else:
                        self.displayErrorMessage()

        except Exception as error:
            print(error)

    # login

    def Login(self):
        try:
            self.HideError()
            self.close()
        except Exception as error:
            print(error)

    # hide error

    def HideError(self):
        try:
            self.ui.error_label.setHidden(True)
        except Exception as error:
            print(error)

    # display password error

    def displayPasswordErrorMessage(self):
        try:
            self.ui.error_label.setText("Password should be 8 characters long")
            self.ui.error_label.setHidden(False)
        except Exception as error:
            print(error)

    # display error on null input

    def displayErrorMessage(self):
        try:
            self.ui.error_label.setText("Enter Your Registered Email")
            self.ui.error_label.setHidden(False)
        except Exception as error:
            print(error)

    # change password

    def ChangePassword(self):
        try:
            conn = createConnection()
            connection = conn.cursor()
            query = '''Update RAASIET_QuizApp.dbo.tbl_admin set admin_password=?  WHERE admin_email=? '''
            connection.execute(query, self.passwordInput, self.emailInput)
            conn.commit()
            self.msgBox.setWindowIcon(QtGui.QIcon(':/Icons/icons/Logo/logo-the-hunar-foundation.jpg'))
            self.msgBox.setWindowTitle("Change Password")
            self.msgBox.setText("Password Changed Successfully")
            self.msgBox.exec_()
            self.Login()
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ForgotPasswordWindow()
    sys.exit(app.exec_())
