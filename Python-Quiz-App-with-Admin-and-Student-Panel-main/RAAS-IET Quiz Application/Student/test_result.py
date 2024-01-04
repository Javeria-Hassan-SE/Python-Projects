from PyQt5 import QtCore, QtGui, QtWidgets
from database_connection import *
import icon_rc
import SharedPreferences
from PyQt5.QtWidgets import *
import sys
from UI_test_result import Ui_Result
import re
from datetime import datetime


class ResultWindow(QMainWindow):

    # UI Initialize

    def __init__(self, parent=None):
        try:
            QMainWindow.__init__(self)
            self.ui = Ui_Result()
            self.ui.setupUi(self)
            self.show()
            self.ui.exit_app_btn.clicked.connect(self.exit)
            self.result_status = ""
            self.result_type = ""
            self.attemp_1_test_date = ""
            self.attemp_2_test_date = None
            self.attemp2_is_allowed_Yes = "Yes"
            self.attemp2_is_allowed_No = "No"
            self.std_attempt1 = 1
            self.std_attempt2_yes = 2
            self.std_attempt2_no = 0
            self.obtainedMarks = 0
            self.TotalMarks = SharedPreferences.total_marks
            self.percentage = 0
            self.saveResult()
            self.fetchResult()
            self.displayResult()

        except Exception as error:
            print(error)

    # check is attempt 1 of user

    def isAttempt1(self):
        try:
            query = "SELECT std_obt_marks , attemp2_is_allowed, std_attempt1, std_attempt2 FROM " \
                    "RAASIET_QuizApp.dbo.tbl_std_answers where " \
                    "std_id_FK=? and attemp2_is_allowed=? and std_attempt1=? and std_attempt2=?"
            conn = createConnection()
            connection = conn.cursor()
            connection.execute(query, SharedPreferences.std_id, self.attemp2_is_allowed_No, self.std_attempt1,
                               self.std_attempt2_no)
            rows = connection.fetchall()
            conn.commit()
            if rows is not None:
                self.student_obt_marks = []
                for row in rows:
                    self.student_obt_marks.append(row.std_obt_marks)
                    self.result_type = "Attempt 1"
                    self.attemp_1_test_date = datetime.now()
                    self.attemp_2_test_date = None

                self.total_obt_marks = sum(self.student_obt_marks)
                self.total_obt_marks = float(self.total_obt_marks)
                self.TotalMarks = float(self.TotalMarks)
                self.percentage = (self.total_obt_marks * 100) / self.TotalMarks
                self.percentage = float(self.percentage)

                if self.percentage >= 60.0:
                    self.result_status = "PASSED"
                else:
                    self.result_status = "FAILED"
        except Exception as error:
            print(error)

    # check is attempt 2 allowed to this student or not

    def checkIfAttempt2Allowed(self):
        try:
            conn = createConnection()
            if conn is not None:
                connection = conn.cursor()
                query = '''Select test_attempt2_is_allowed From RAASIET_QuizApp.dbo.tbl_entry_test_students Where ID 
                = ? '''
                connection.execute(query, SharedPreferences.std_id)
                data = connection.fetchone()
                conn.commit()
                if data is not None:
                    if data.test_attempt2_is_allowed == "Yes":
                        return True
                else:
                    return False
        except Exception as error:
            print(error)

    # check is attempt 2

    def isAttempt2(self):
        try:
            query1 = "SELECT attemp_1_test_date FROM RAASIET_QuizApp.dbo.tbl_std_result where std_id_FK=? "
            conn1 = createConnection()
            connection1 = conn1.cursor()
            connection1.execute(query1, SharedPreferences.std_id)
            data = connection1.fetchone()
            conn1.commit()
            self.attemp_1_test_date = data.attemp_1_test_date

            query = "SELECT std_obt_marks , attemp2_is_allowed, std_attempt1, std_attempt2 FROM " \
                    "RAASIET_QuizApp.dbo.tbl_std_answers where " \
                    "std_id_FK=? and attemp2_is_allowed=? and std_attempt1=? and std_attempt2=?"
            conn = createConnection()
            connection = conn.cursor()
            connection.execute(query, SharedPreferences.std_id, self.attemp2_is_allowed_Yes, self.std_attempt1,
                               self.std_attempt2_yes)
            rows2 = connection.fetchall()
            conn.commit()
            if rows2 is not None:
                self.student_obt_marks = []
                for row in rows2:
                    self.student_obt_marks.append(row.std_obt_marks)
                    self.result_type = "Attempt 2"
                    self.attemp_2_test_date = datetime.now()

                self.total_obt_marks = sum(self.student_obt_marks)
                self.percentage = (self.total_obt_marks * 100) / self.TotalMarks
                self.total_obt_marks = sum(self.student_obt_marks)
                self.total_obt_marks = float(self.total_obt_marks)
                self.TotalMarks = float(self.TotalMarks)
                self.percentage = (self.total_obt_marks * 100) / self.TotalMarks
                self.percentage = float(self.percentage)

                if self.percentage >= 60.0:
                    self.result_status = "PASSED"
                else:
                    self.result_status = "FAILED"
        except Exception as error:
            print(error)

    # save result in db

    def saveResult(self):
        try:
            if self.checkIfAttempt2Allowed():
                self.isAttempt2()

            else:
                self.isAttempt1()

            query = '''INSERT into RAASIET_QuizApp.dbo.tbl_std_result (std_id_FK,std_name,  total_marks, obt_marks, 
            percentage, result_status,result_type, attemp_1_test_date, attemp_2_test_date) VALUES (?,?,?,?,?,?,?,?,
            ?) '''
            conn1 = createConnection()
            connection1 = conn1.cursor()
            connection1.execute(query, SharedPreferences.std_id, SharedPreferences.std_name, self.TotalMarks,
                                self.total_obt_marks, self.percentage, self.result_status, self.result_type,
                                self.attemp_1_test_date, self.attemp_2_test_date)
            conn1.commit()
        except Exception as error:
            print(error)

    # fetch result

    def fetchResult(self):
        try:
            query = "SELECT total_marks, obt_marks, percentage FROM RAASIET_QuizApp.dbo.tbl_std_result where " \
                    "std_id_FK=? "
            conn = createConnection()
            connection = conn.cursor()
            connection.execute(query, SharedPreferences.std_id)
            rows = connection.fetchall()
            for row in rows:
                self.obtainedMarks = row.obt_marks
                self.TotalMarks = row.total_marks
                self.percentage = row.percentage

            conn.commit()
        except Exception as error:
            print(error)

    # display result

    def displayResult(self):
        try:
            self.obtainedMarks = str(self.obtainedMarks)
            self.TotalMarks = str(self.TotalMarks)
            self.percentage = str(self.percentage)
            self.ui.disp_std_name_label.setText("Dear " + SharedPreferences.std_name)
            # self.ui.show_obt_marks_label.setText(self.obtainedMarks)
            # self.ui.show_total_marks_label.setText(self.TotalMarks)
            self.ui.scored_marks_label.setText("You have scored " + self.percentage + "% marks.")
            self.update_std_record()
        except Exception as error:
            print(error)

    # exit app

    def exit(self):
        try:
            self.close()
        except Exception as error:
            print(error)

    # update std record that he/she has attempt 2

    def update_std_record(self):
        try:
            conn = createConnection()
            if conn is not None:
                connection = conn.cursor()
                query = '''Update RAASIET_QuizApp.dbo.tbl_entry_test_students set std_has_attempt_test=? where ID = ?'''
                connection.execute(query, "Yes", SharedPreferences.std_id)
                conn.commit()
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ResultWindow()
    sys.exit(app.exec_())
