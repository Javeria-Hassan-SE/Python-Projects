from PyQt5 import QtCore, QtGui, QtWidgets
from database_connection import *
import icon_rc
import SharedPreferences
from PyQt5.QtWidgets import *
import sys
from UI_student_login import Ui_Login
import re
from datetime import datetime
from test_options import *


class StudentLoginWindow(QMainWindow):

    # UI Initialize

    def __init__(self, parent=None):
        try:
            QMainWindow.__init__(self)
            self.ui = Ui_Login()
            self.ui.setupUi(self)
            self.show()

            self.HideErrorMessage()
            self.btnClicked()
        except Exception as error:
            print(error)

    # btn clicked to relevant functions

    def btnClicked(self):
        try:
            self.ui.login_btn.clicked.connect(self.validateInput)
        except Exception as error:
            print(error)

    # hide error message

    def HideErrorMessage(self):
        try:
            self.ui.error_label.setHidden(True)

        except Exception as error:
            print(error)

    # display error message

    def displayErrorMessage(self):
        try:
            self.ui.error_label.setText("Invalid Email or Password")
            self.ui.error_label.setStyleSheet("color: red; font-size: 13pt")
            self.ui.error_label.setHidden(False)
        except Exception as error:
            print(error)

    # display success message

    def displaySuccessMessage(self):
        try:
            self.ui.error_label.setHidden(False)
            self.ui.error_label.setText("Successful Login")
            self.ui.error_label.setStyleSheet("color: white;")
            self.ui.ID_lineEdit.setText("")
        except Exception as error:
            print(error)

    # input Validation

    def validateInput(self):

        try:
            self.ID_Input = str(self.ui.ID_lineEdit.text())
            self.password_Input = str(self.ui.password_line_edit.text())
            if self.ID_Input == "" or self.password_Input == "":
                #self.displayErrorMessage()
                self.showPanel()
            else:
                self.Login()
        except Exception as error:
            print(error)

    # login

    def Login(self):
        try:
            conn = createConnection()
            if conn is not None:
                connection = conn.cursor()
                connection.execute(
                    "SELECT ID, Name, std_password, std_email FROM RAASIET_QuizApp.dbo.entry_test_students_id_pass "
                    "where ID = ? and "
                    "std_password = ?",
                    (self.ID_Input, self.password_Input))
                data = connection.fetchone()
                conn.commit()
                if data is not None:
                    SharedPreferences.std_id = data.ID
                    SharedPreferences.std_name = data.Name
                    SharedPreferences.email = data.std_email
                    self.displaySuccessMessage()
                    self.showPanel()
                else:
                    self.displayErrorMessage()
        except Exception as error:
            print(error)

    # show instructions panel

    def showPanel(self):
        try:
            self.ui_instructions = TestOptionsWindow()
            self.close()
        except Exception as error:
            print(error)

    # show register window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentLoginWindow()
    sys.exit(app.exec_())
