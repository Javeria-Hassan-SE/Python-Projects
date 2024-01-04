from PyQt5.QtWidgets import *
from UI_entry_test_quiz import Ui_EntryTest
from test_result import *
from database_connection import *
import SharedPreferences
from PyQt5 import QtCore, QtGui, QtWidgets
import icon_rc
import random
import time
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import os
from datetime import datetime
import threading


class QuizWindow(QMainWindow):

    # Initialize UI

    def __init__(self, parent=None):
        try:
            QMainWindow.__init__(self)
            self.ui = Ui_EntryTest()
            self.ui.setupUi(self)
            self.attemp2_is_allowed = "No"
            self.std_attempt1 = 1
            self.std_attempt2 = 0
            self.show()
            self.HideErrorMessage()
            self.resetUI()
            self.ui.disp_std_name_label.setText(SharedPreferences.std_name)
            self.fetchTotalTime_and_TotalMarks()
            self.fetchQuestion()
            self.btnClicked()
        except Exception as error:
            print(error)

    # btn clicked to relevant functions

    def btnClicked(self):
        try:
            self.ui.next_btn.clicked.connect(self.nextQuestion)
        except Exception as error:
            print(error)

    # show next question

    def nextQuestion(self):
        try:
            self.addData()
            self.resetUI()
            self.clearData()
            self.UnCheckRadioButtons()
            self.fetchQuestion()

        except Exception as error:
            print(error)

    # fetch total number of questions from database and set time according to that

    def fetchTotalTime_and_TotalMarks(self):
        try:
            query = "SELECT q_id FROM RAASIET_QuizApp.dbo.tbl_entry_test_questions where q_status =?"
            conn = createConnection()
            connection = conn.cursor()
            connection.execute(query, "active")
            rows = connection.fetchall()
            conn.commit()
            self.q_no_list = []
            self.q_row_len = []

            for i in rows:
                self.q_row_len.append(len(i))
                self.q_no_list.append(i.q_id)
            self.total_time = len(self.q_row_len)
            self.total_marks = len(self.q_row_len)
            SharedPreferences.total_marks = self.total_marks
            thread = threading.Thread(target=self.runTimer)
            thread.start()
        except Exception as error:
            print(error)

    # generate random questions from total questions list

    def generateRandomQuestion(self):
        try:
            if self.q_no_list:
                self.random_question = random.choice(self.q_no_list)

            if not self.q_no_list:
                self.ui.next_btn.setText("Submit")
                self.clearData()
                self.showPanel()
        except Exception as error:
            print(error)

    # Uncheck radio buttons

    def UnCheckRadioButtons(self):
        try:
            self.ui.option1_radioButton.setAutoExclusive(False)
            self.ui.option2_radioButton.setAutoExclusive(False)
            self.ui.option3_radioButton.setAutoExclusive(False)
            self.ui.option4_radioButton.setAutoExclusive(False)
            self.ui.option1_radioButton.setChecked(False)
            self.ui.option2_radioButton.setChecked(False)
            self.ui.option3_radioButton.setChecked(False)
            self.ui.option4_radioButton.setChecked(False)

        except Exception as error:
            print(error)

    # clear all data when next button pressed

    def clearData(self):
        try:
            self.ui.question_display_label.setText("")
            self.ui.question_image_label.clear()
            self.ui.question_image_label.setText("")
            self.ui.option1_radioButton.setText("")
            self.ui.option2_radioButton.setText("")
            self.ui.option3_radioButton.setText("")
            self.ui.option4_radioButton.setText("")

        except Exception as error:
            print(error)

    # show result panel

    def showPanel(self):
        try:
            self.ui_result = ResultWindow()
            self.close()
        except Exception as error:
            print(error)

    # fetch question and display

    def fetchQuestion(self):
        try:
            self.generateRandomQuestion()
            self.pixmap = QPixmap()
            self.imageBinary = None
            query = "SELECT * FROM RAASIET_QuizApp.dbo.tbl_entry_test_questions Where q_id=?"
            conn = createConnection()
            connection = conn.cursor()
            connection.execute(query, self.random_question)
            self.rows = connection.fetchone()
            if self.rows is not None:
                self.ui.question_display_label.setText(self.rows.question)
                self.ui.option1_radioButton.setText(self.rows.opt_1_txt)
                self.ui.option2_radioButton.setText(self.rows.opt_2_txt)
                self.ui.option3_radioButton.setText(self.rows.opt_3_txt)
                self.ui.option4_radioButton.setText(self.rows.opt_4_txt)
                if self.rows.q_img is not None:
                    self.binarydata = self.rows.q_img
                    self.pixmap.loadFromData(self.loadImage())
                    self.ui.question_image_label.setPixmap(self.pixmap)

                if self.rows.opt_1_txt == "":
                    self.ui.option1_radioButton.setText("option 1")
                    self.ui.option1_radioButton.setGeometry(QtCore.QRect(140, 370, 321, 51))
                    #self.ui.disp_opt_1_img.setHidden(False)

                if self.rows.opt_2_txt == "":
                    self.ui.option2_radioButton.setText("option 2")
                    self.ui.option2_radioButton.setGeometry(QtCore.QRect(140, 440, 321, 51))
                    #self.ui.disp_opt_2_img.setHidden(False)

                if self.rows.opt_3_txt == "":
                    self.ui.option3_radioButton.setText("option 3")
                    self.ui.option3_radioButton.setGeometry(QtCore.QRect(140, 510, 321, 51))
                    #self.ui.disp_opt_3_img.setHidden(False)

                if self.rows.opt_4_txt == "":
                    self.ui.option4_radioButton.setText("option 4")
                    self.ui.option4_radioButton.setGeometry(QtCore.QRect(140, 580, 91, 51))
                    #self.ui.disp_opt_4_img.setHidden(False)

                if self.rows.opt_1_img is not None:
                    self.binarydata = self.rows.opt_1_img
                    self.pixmap.loadFromData(self.loadImage())
                    #self.ui.disp_opt_1_img.setPixmap(self.pixmap)

                if self.rows.opt_2_img is not None:
                    self.binarydata = self.rows.opt_2_img
                    self.pixmap.loadFromData(self.loadImage())
                    #self.ui.disp_opt_2_img.setPixmap(self.pixmap)

                if self.rows.opt_3_img is not None:
                    self.binarydata = self.rows.opt_3_img
                    self.pixmap.loadFromData(self.loadImage())
                    #self.ui.disp_opt_3_img.setPixmap(self.pixmap)

                if self.rows.opt_4_img is not None:
                    self.binarydata = self.rows.opt_4_img
                    self.pixmap.loadFromData(self.loadImage())
                    #self.ui.disp_opt_4_img.setPixmap(self.pixmap)

                if self.rows.opt_4_txt == "" and self.rows.opt_4_img is None:
                    self.ui.option4_radioButton.setText("")
                    self.ui.option4_radioButton.setHidden(True)

            conn.commit()
        except Exception as error:
            print(error)

    # reset UI on next btn clicked

    def resetUI(self):
        try:
            self.ui.option1_radioButton.setGeometry(QtCore.QRect(140, 370, 701, 51))
            self.ui.option2_radioButton.setGeometry(QtCore.QRect(140, 440, 701, 51))
            self.ui.option3_radioButton.setGeometry(QtCore.QRect(140, 510, 701, 51))
            self.ui.option4_radioButton.setGeometry(QtCore.QRect(140, 580, 711, 51))
            self.ui.option4_radioButton.setHidden(False)

        except Exception as error:
            print(error)

    # load image if present

    def loadImage(self):
        try:
            n = random.randint(0, 10000)
            n = str(n)
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            StoreFilePath = desktop + '\Images'
            if not os.path.exists(StoreFilePath):
                os.makedirs(StoreFilePath)
            else:
                StoreFilePath = desktop + '\Images\ ' + n + ".png"
                with open(StoreFilePath, "wb") as File:
                    File.write(self.binarydata)
                    File.close()
                with open(StoreFilePath, 'rb') as f:
                    return f.read()
        except Exception as error:
            print(error)

    # get student answer

    def getStudentAnswer(self):
        try:
            self.stdAnswer = ""
            if self.ui.option1_radioButton.isChecked():
                self.stdAnswer = self.ui.option1_radioButton.text()
            elif self.ui.option2_radioButton.isChecked():
                self.stdAnswer = self.ui.option2_radioButton.text()
            elif self.ui.option3_radioButton.isChecked():
                self.stdAnswer = self.ui.option3_radioButton.text()
            elif self.ui.option4_radioButton.isChecked():
                self.stdAnswer = self.ui.option4_radioButton.text()
            if self.stdAnswer == "option 1":
                self.imageBinary = self.rows.opt_1_img
                self.stdAnswer = ""
            if self.stdAnswer == "option 2":
                self.imageBinary = self.rows.opt_2_img
                self.stdAnswer = ""
            if self.stdAnswer == "option 3":
                self.imageBinary = self.rows.opt_3_img
                self.stdAnswer = ""
            if self.stdAnswer == "option 4":
                self.imageBinary = self.rows.opt_4_img
                self.stdAnswer = ""
            else:
                self.displayErrorMessage()

        except Exception as error:
            print(error)

    # display error message

    def displayErrorMessage(self):
        try:
            print("Error")
        except Exception as error:
            print(error)

    # hide error

    def HideErrorMessage(self):
        try:
            print("Hide Error")
        except Exception as error:
            print(error)

    # get attempt to check for which attempt student is giving test

    def getAttempt(self):
        try:
            conn = createConnection()
            if conn is not None:
                connection = conn.cursor()
                connection.execute(
                    "SELECT test_attempt2_is_allowed FROM RAASIET_QuizApp.dbo.tbl_entry_test_students where ID = ? ",
                    (SharedPreferences.std_id))
                data = connection.fetchone()
                conn.commit()
                if data is not None:
                    if data.test_attempt2_is_allowed == "Yes":
                        self.attemp2_is_allowed = "Yes"
                        self.std_attempt1 = 1
                        self.std_attempt2 = 2

                    else:
                        self.attemp2_is_allowed = "No"
                        self.std_attempt1 = 1
                        self.std_attempt2 = 0

        except Exception as error:
            print(error)

    # add student answer

    def addData(self):
        try:
            self.getStudentAnswer()
            self.getAttempt()
            if self.stdAnswer != "" or self.imageBinary is not None:
                self.HideErrorMessage()
                self.added_on = datetime.now()
                query = "SELECT question,q_section, q_right_answer_txt, q_right_answer_img FROM " \
                        "RAASIET_QuizApp.dbo.tbl_entry_test_questions where " \
                        "q_id=? "
                conn = createConnection()
                connection = conn.cursor()
                connection.execute(query, self.random_question)
                rows = connection.fetchone()
                conn.commit()
                if rows != None:
                    self.question = rows.question
                    self.q_section = rows.q_section
                    self.rightAnswer = rows.q_right_answer_txt

                    if rows.q_right_answer_txt != "":
                        if self.stdAnswer == self.rightAnswer:
                            self.is_ans_right = True
                            self.obt_marks = 1
                        else:
                            self.is_ans_right = False
                            self.obt_marks = 0

                    else:
                        if rows.q_right_answer_img != "":
                            if self.imageBinary == rows.q_right_answer_img:
                                self.is_ans_right = True
                                self.obt_marks = 1
                            else:
                                self.is_ans_right = False
                                self.obt_marks = 0

                conn1 = createConnection()
                connection = conn1.cursor()
                query = '''INSERT INTO RAASIET_QuizApp.dbo.tbl_std_answers (q_id_FK, question, question_section, std_id_FK, 
                        std_answer_txt, std_answer_img, std_obt_marks,ans_is_right,answered_on,
                         attemp2_is_allowed,std_attempt1,std_attempt2)
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''
                connection.execute(query, self.random_question, self.question, self.q_section, SharedPreferences.std_id,
                                   self.stdAnswer,
                                   self.imageBinary,
                                   self.obt_marks,
                                   self.is_ans_right, self.added_on, self.attemp2_is_allowed, self.std_attempt1,
                                   self.std_attempt2)
                conn1.commit()

                index = self.q_no_list.index(self.random_question)
                self.q_no_list.pop(index)

            else:
                self.displayErrorMessage()
        except Exception as error:
            print(error)

    # run timer

    def runTimer(self):
        try:
            self.seconds = self.total_time * 60
            for self.remaining in range(self.seconds, 0, -1):
                self.minutes = 0
                self.seconds = self.remaining
                if self.remaining > 60:
                    self.minutes = int(self.seconds / 60)
                    self.seconds = int(self.seconds % 60)
                else:
                    self.seconds = self.remaining
                self.ui.disp_time_label.setText(
                    "{:2d} minutes {:2d} seconds remaining.".format(self.minutes, self.seconds))
                sys.stdout.flush()
                time.sleep(1)
            self.ui.disp_time_label.setText("Timer complete")
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizWindow()
    sys.exit(app.exec_())
