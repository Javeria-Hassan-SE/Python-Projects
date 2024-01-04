from PyQt5 import QtGui
from database_connection import *
import icon_rc
import SharedPreferences
from PyQt5.QtWidgets import *
import sys
from UI_instructions import Ui_Instructions
from entry_test_quiz import *


class InstructionsWindow(QMainWindow):

    # UI Initialize

    def __init__(self, parent=None):
        try:
            QMainWindow.__init__(self)
            self.ui = Ui_Instructions()
            self.ui.setupUi(self)
            self.show()
            self.btnClicked()
        except Exception as error:
            print(error)

    # btn Clicked

    def btnClicked(self):
        try:
            self.ui.class_test_btn.clicked.connect(self.std_already_has_given_test)
        except Exception as error:
            print(error)

    # check if student has already given the test

    def std_already_has_given_test(self):
        try:
            conn = createConnection()
            if conn is not None:
                connection = conn.cursor()
                connection.execute(
                    "SELECT std_id_FK FROM RAASIET_QuizApp.dbo.tbl_std_result where std_id_FK = ? ",
                    SharedPreferences.std_id)
                data = connection.fetchone()
                conn.commit()
                if data is not None:
                    if SharedPreferences.std_id == data.std_id_FK:
                        conn1 = createConnection()
                        connection1 = conn1.cursor()
                        connection1.execute(
                            "SELECT test_attempt2_is_allowed FROM RAASIET_QuizApp.dbo.tbl_entry_test_students where "
                            "ID = ? ",
                            SharedPreferences.std_id)
                        data1 = connection1.fetchone()
                        conn1.commit()
                        if data1 is not None:
                            if data1.test_attempt2_is_allowed == "No":
                                self.displayErrorMessage()
                            else:
                                conn3 = createConnection()
                                connection3 = conn3.cursor()
                                connection3.execute(
                                    "SELECT std_attempt2 FROM RAASIET_QuizApp.dbo.tbl_std_answers where std_id_FK = ?",
                                    SharedPreferences.std_id)
                                data = connection3.fetchall()
                                conn3.commit()
                                self.attemptlist=[]
                                for row in data:
                                    self.attemptlist.append(row.std_attempt2)
                                if 2 in self.attemptlist:
                                    self.displayAttempt2ErrorMessage()
                                else:
                                    self.showPanel()
                else:
                    self.showPanel()
        except Exception as error:
            print(error)

    # show quiz panel

    def showPanel(self):
        try:
            self.ui_quiz = QuizWindow()
            self.close()
        except Exception as error:
            print(error)

    # display error message if student has already attempt the test

    def displayErrorMessage(self):
        try:
            self.msg = QMessageBox()
            self.msg.setWindowIcon(QtGui.QIcon(':/Icons/icons/Logo/logo-the-hunar-foundation.jpg'))
            self.msg.setWindowTitle("Error")
            self.msg.setText("You have Already given the test or attempt 2 is not allowed")
            self.msg.exec_()
            self.close()
        except Exception as error:
            print(error)

    # display error message if student has already attempt the test 2 times

    def displayAttempt2ErrorMessage(self):
        try:
            self.msg = QMessageBox()
            self.msg.setWindowIcon(QtGui.QIcon(':/Icons/icons/Logo/logo-the-hunar-foundation.jpg'))
            self.msg.setWindowTitle("Error")
            self.msg.setText("Sorry! You have Already attempt the test 2 times")
            self.msg.exec_()
            self.close()
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstructionsWindow()
    sys.exit(app.exec_())
