from PyQt5 import QtCore, QtGui, QtWidgets
from database_connection import *
import icon_rc
import SharedPreferences
from PyQt5.QtWidgets import *
import sys
from UI_add_question import Ui_AddQuestionWindow
import re
from datetime import datetime
import os


class AddQuestionWindow(QMainWindow):

    # UI Initialization

    def __init__(self, parent=None):
        try:
            QMainWindow.__init__(self)
            self.ui = Ui_AddQuestionWindow()
            self.ui.setupUi(self)
            self.show()
            self.questionImageBinary = None
            self.Option1ImageBinary = None
            self.Option2ImageBinary = None
            self.Option3ImageBinary = None
            self.Option4ImageBinary = None
            self.right_ans_imgBinary = None
            self.fetchQuestionSection()
            self.ImagePath = ""
            self.added_on = datetime.now()
            self.ImageBinaryData = None
            self.clickedButtonName = ""
            self.get_q_status_txt_combo = ""
            self.get_section_txt_combo = ""
            self.get_section_txt = "No section Selected"
            self.get_q_status_txt = "active"
            self.msg = QMessageBox()
            self.HideErrorMessage()
            self.btnClicked()

        except Exception as error:
            print(error)

    # Hide Error Message

    def HideErrorMessage(self):
        try:
            self.ui.dis_error_msg.setHidden(True)


        except Exception as error:
            print(error)

    # btn clicked to relevant function

    def btnClicked(self):
        try:
            self.ui.add_question_btn.clicked.connect(self.validateInput)
            self.ui.q_img_btn.clicked.connect(self.getQuestionButtonName)
            self.ui.opt1_img_btn.clicked.connect(self.getOption1ButtonName)
            self.ui.opt2_img_btn.clicked.connect(self.getOption2ButtonName)
            self.ui.opt3_img_btn.clicked.connect(self.getOption3ButtonName)
            self.ui.opt4_img_btn.clicked.connect(self.getOption4ButtonName)
            self.ui.right_ans_img_btn.clicked.connect(self.getAnswerButtonName)
            self.ui.q_status_combo_box.activated[str].connect(self.get_q_status)
            self.ui.q_section_combo_box.activated[str].connect(self.get_section)

        except Exception as error:
            print(error)

    # fetch sections in combo box

    def fetchQuestionSection(self):
        try:
            self.ui.q_section_combo_box.clear()
            query = "SELECT q_sec_text FROM RAASIET_QuizApp.dbo.q_section"
            conn = createConnection()
            connection = conn.cursor()
            connection.execute(query)
            rows = connection.fetchall()
            self.section_list = []
            if rows != None:
                for row in rows:
                    self.section_list.append(row.q_sec_text)
                self.ui.q_section_combo_box.addItems(self.section_list)
            else:
                self.section_list = ["No section Selected"]
                self.ui.q_section_combo_box.addItems(self.section_list)

        except Exception as error:
            print(error)

    # get question status active , de-active

    def get_q_status(self):
        try:
            self.get_q_status_txt_combo = self.ui.q_status_combo_box.currentText()
        except Exception as error:
            self.get_q_status_txt_combo = self.get_q_status_txt
            print(error)

    # get user selected question section

    def get_section(self):
        try:
            self.get_section_txt_combo = self.ui.q_section_combo_box.currentText()
        except Exception as error:
            self.get_section_txt_combo = self.get_section_txt
            print(error)

    # ================================ get browse button name for identifying image selection =======================

    def getQuestionButtonName(self):
        try:
            self.clickedButtonName = "Browse Question Image"
            self.getBrowseButtonText()

        except Exception as error:
            print(error)

    def getOption1ButtonName(self):
        try:
            self.clickedButtonName = "Browse Option 1 Image"
            self.getBrowseButtonText()

        except Exception as error:
            print(error)

    def getOption2ButtonName(self):
        try:
            self.clickedButtonName = "Browse Option 2 Image"
            self.getBrowseButtonText()

        except Exception as error:
            print(error)

    def getOption3ButtonName(self):
        try:
            self.clickedButtonName = "Browse Option 3 Image"
            self.getBrowseButtonText()
        except Exception as error:
            print(error)

    def getOption4ButtonName(self):
        try:
            self.clickedButtonName = "BrowseOption 4 Image"
            self.getBrowseButtonText()

        except Exception as error:
            print(error)

    def getAnswerButtonName(self):
        try:
            self.clickedButtonName = "Browse Right Answer Image"
            self.getBrowseButtonText()
        except Exception as error:
            print(error)

    def getBrowseButtonText(self):
        try:
            self.launchDialog()
            if self.clickedButtonName == "Browse Question Image":
                self.ui.q_img_path_label.setText(self.ImagePath)
                self.questionImageBinary = self.ImageBinaryData

            elif self.clickedButtonName == "Browse Option 1 Image":
                self.ui.opt1img_path_label.setText(self.ImagePath)
                self.Option1ImageBinary = self.ImageBinaryData

            elif self.clickedButtonName == "Browse Option 2 Image":
                self.ui.opt2_img_path_label.setText(self.ImagePath)
                self.Option2ImageBinary = self.ImageBinaryData

            elif self.clickedButtonName == "Browse Option 3 Image":
                self.ui.opt3_img_path_label.setText(self.ImagePath)
                self.Option3ImageBinary = self.ImageBinaryData

            elif self.clickedButtonName == "BrowseOption 4 Image":
                self.ui.opt4_img_path_label.setText(self.ImagePath)
                self.Option4ImageBinary = self.ImageBinaryData

            elif self.clickedButtonName == "Browse Right Answer Image":
                self.ui.right_ans_img_path_label.setText(self.ImagePath)
                self.right_ans_imgBinary = self.ImageBinaryData
            else:
                self.ui.q_img_path_label.setText("")
                self.ui.opt1img_path_label.setText("")
                self.ui.opt2_img_path_label.setText("")
                self.ui.opt3_img_path_label.setText("")
                self.ui.opt4_img_path_label.setText("")
                self.ui.right_ans_img_path_label.setText("")

        except Exception as error:
            print(error)

    # open choose file dialogue

    def launchDialog(self):
        try:
            self.ImagePath = self.getFileName()
            print(self.ImagePath)
            self.ImageBinaryData = self.getImageBinaryData()
            print(self.ImageBinaryData)

        except Exception as error:
            print(error)
            self.ImagePath = ""
            self.ImageBinaryData = None

    # get user selected image name

    def getFileName(self):
        try:
            file_filter = 'Image File (*.png)'
            response = QFileDialog.getOpenFileName(
                parent=None,
                caption='Select an Image',
                directory=os.getcwd(),
                filter=file_filter,
                initialFilter='Image File (*.png)'
            )
            return response[0]

        except Exception as error:
            print(error)

    # convert image into binary format

    def getImageBinaryData(self):
        try:
            with open(self.ImagePath, "rb") as File:
                BinaryImgData = File.read()
                return BinaryImgData
        except Exception as error:
            print(error)

    # get which is right answer from radio button checked

    def getRightAnswer(self):
        try:
            self.rightAnswer = ""
            if self.ui.opt1_radioButton.isChecked():
                self.rightAnswer = str(self.ui.option1_lineEdit.text())
            elif self.ui.opt2_radioButton.isChecked():
                self.rightAnswer = str(self.ui.option2_line_edit.text())
            elif self.ui.opt3_radioButton.isChecked():
                self.rightAnswer = str(self.ui.option3_lineEdit.text())
            elif self.ui.opt4_radioButton.isChecked():
                self.rightAnswer = str(self.ui.option4_lineEdit.text())

        except Exception as error:
            print(error)

    # input validation

    def validateInput(self):
        try:
            self.question = str(self.ui.question_text_edit.toPlainText())
            self.option1 = str(self.ui.option1_lineEdit.text())
            self.option2 = str(self.ui.option2_line_edit.text())
            self.option3 = str(self.ui.option3_lineEdit.text())
            self.option4 = str(self.ui.option4_lineEdit.text())
            self.marks = str(self.ui.q_marks_spinBox.text())
            self.getRightAnswer()

            if self.get_q_status_txt_combo == "":
                self.get_q_status_txt_combo = self.get_q_status_txt

            if self.get_section_txt_combo == "":
                self.get_section_txt_combo = self.get_section_txt

            if self.question == "" or self.marks == "" or (self.option1 == "" and self.ui.opt1img_path_label == "") or (
                    self.option2 == "" and self.ui.opt2_img_path_label == "") or (
                    self.option3 == "" and self.ui.opt3_img_path_label == "") or (
                    self.rightAnswer == "" and self.ui.right_ans_img_path_label == ""):
                self.HideErrorMessage()
                self.displayErrorMessage()
                if self.get_section_txt_combo == "No section Selected":
                    self.SectionErrorMessage()

            if self.get_section_txt_combo != "No section Selected" and self.question != "" and self.marks != "" and (
                    self.option1 != "" or self.ui.opt1img_path_label != "") and (
                    self.option2 != "" or self.ui.opt2_img_path_label != "") and (
                    self.rightAnswer != "" or self.ui.right_ans_img_path_label != ""):
                self.AddQuestion()
                self.HideErrorMessage()
            else:
                self.displayErrorMessage()


        except Exception as error:
            print(error)

    # show error if no section is selected

    def SectionErrorMessage(self):
        try:
            self.ui.dis_error_msg.setHidden(False)
            self.ui.dis_error_msg.setText("Please Select Section")
            self.ui.dis_error_msg.setStyleSheet("color: red")

        except Exception as error:
            print(error)

    # show error on invalid input

    def displayErrorMessage(self):
        try:
            self.ui.dis_error_msg.setHidden(False)
            self.ui.dis_error_msg.setText("Please Fill all Fields")

        except Exception as error:
            print(error)

    # add question

    def AddQuestion(self):
        try:
            conn = createConnection()

            connection = conn.cursor()
            query = '''INSERT INTO RAASIET_QuizApp.dbo.tbl_entry_test_questions (question,q_img, opt_1_txt,opt_1_img, 
            opt_2_txt,opt_2_img,opt_3_txt,opt_3_img,opt_4_txt,opt_4_img,q_right_answer_txt,q_right_answer_img, 
            total_marks,q_added_by_name_admin, q_added_by_admin_id_FK,q_added_on, q_status, q_section) VALUES(?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
            connection.execute(query, self.question, self.questionImageBinary, self.option1, self.Option1ImageBinary,
                               self.option2, self.Option2ImageBinary,
                               self.option3, self.Option3ImageBinary, self.option4, self.Option4ImageBinary,
                               self.rightAnswer, self.right_ans_imgBinary,
                               self.marks, SharedPreferences.user_name, SharedPreferences.admin_id, self.added_on,
                               self.get_q_status_txt_combo, self.get_section_txt_combo)
            conn.commit()
            print("text", self.rightAnswer)
            print("binary", self.right_ans_imgBinary)

            self.msg.setWindowIcon(QtGui.QIcon(':/Icons/icons/Logo/logo-the-hunar-foundation.jpg'))
            self.msg.setWindowTitle("Question")
            self.msg.setText("Added Successfully")
            self.msg.exec_()
            self.clearInput()
            self.close()

        except Exception as error:
            print(error)

    # clear input

    def clearInput(self):
        try:
            self.ui.question_text_edit.setText("")
            self.ui.option1_lineEdit.setText("")
            self.ui.option2_line_edit.setText("")
            self.ui.option3_lineEdit.setText("")
            self.ui.option4_lineEdit.setText("")
            self.ui.q_img_path_label.setText("")
            self.ui.opt1img_path_label.setText("")
            self.ui.opt2_img_path_label.setText("")
            self.ui.opt3_img_path_label.setText("")
            self.ui.opt4_img_path_label.setText("")
            self.ui.right_ans_img_path_label.setText("")
            self.ui.opt1_radioButton.setChecked(False)
            self.ui.opt2_radioButton.setChecked(False)
            self.ui.opt3_radioButton.setChecked(False)
            self.ui.opt4_radioButton.setChecked(False)

        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddQuestionWindow()
    sys.exit(app.exec_())
