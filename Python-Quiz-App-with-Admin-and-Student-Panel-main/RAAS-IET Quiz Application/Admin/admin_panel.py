from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem

from database_connection import *
import icon_rc
import SharedPreferences
from PyQt5.QtWidgets import *
import sys
from UI_admin_panel import Ui_AdminPortal
import admin_login
import add_question
import re
from datetime import datetime
from PyQt5.QtWidgets import QFileDialog, QDialog
import os
import pandas as pd
import numpy as np
from add_student_for_entry_test import AddStudentForEntryTestWindow
from show_entry_test_students import ShowEntryTestStudentsWindow
from show_students_password import ShowStudentsPasswordWindow
import smtplib


class AdminPanelWindow(QMainWindow):

    # UI Initialization

    def __init__(self, parent=None):
        try:
            QMainWindow.__init__(self)
            self.ui = Ui_AdminPortal()
            self.ui.setupUi(self)
            self.msgBox = QMessageBox()
            self.current_time = datetime.now()
            self.UiVisibility()
            self.btnClicked()
            self.enableTableRowSelection()
            self.initializePages()
            self.showLoginUserName()
            self.show()
            self.added_on = datetime.now()
            self.get_admin_role_txt_combo = ""
            self.get_admin_status_txt_combo = ""
            self.get_admin_status_txt = "active"
            self.get_admin_role_txt = "Instructor"
            self.get_course_instructor_txt_combo = "None"
            self.get_course_preRequired_txt_combo = "None"
            self.emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|org|edu.pk|edu.com|com.pk)+\b'
            self.str_regx = r'\b[A-Za-z ]+'
            self.model = QStandardItemModel(self.ui.show_sections_listView)
            #app.aboutToQuit.connect(self.closeEvent)


        except Exception as error:
            print(error)

    def closeEvent(self):
        # Your desired functionality here
        print('Close button pressed')
        sys.exit(0)
    # enable table row selection when user click in
    # any column of table widget to select first column value of that table which is ID
    def UiVisibility(self):
        self.ui.show_assessments_tableWidget.setHidden(True)
        self.ui.show_no_of_assessmnetslistWidget.setHidden(True)
        self.ui.delete_assessment_btn.setHidden(True)
        self.ui.update_assessments_btn.setHidden(True)
        self.ui.refresh_assessments_btn.setHidden(True)
        self.ui.download_assessment_btn.setHidden(True)

    def enableTableRowSelection(self):
        try:
            self.ui.show_course_students_record_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
            self.ui.show_entry_test_paper_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
            self.ui.view_result_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
            self.ui.show_entryTest_paper_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
            self.ui.show_all_std_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
            self.ui.show_instructor_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
            self.ui.show_courses_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
            self.ui.show_assessments_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
            self.ui.show_course_students_record_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
            self.ui.show_course_wise_result_table.setSelectionBehavior(QTableWidget.SelectRows)
            self.ui.show_searchResult_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
            self.model = QStandardItemModel(self.ui.show_sections_listView)
        except Exception as error:
            print(error)

    # button clicked relevant functions call

    def btnClicked(self):
        try:
            self.ui.upload_entry_test_std_csv_btn.clicked.connect(self.upload_csv)
            self.ui.dashboard_btn.clicked.connect(self.showDashboard)
            self.ui.my_profile_btn.clicked.connect(self.showMyProfile)
            self.ui.instructors_btn.clicked.connect(self.showInstructors)
            self.ui.students_btn.clicked.connect(self.showStudents)
            self.ui.courses_btn.clicked.connect(self.showCourses)
            self.ui.entry_test_button.clicked.connect(self.showEntryTestPage)
            self.ui.logout_btn.clicked.connect(self.logout)
            self.ui.update_profile_btn.clicked.connect(self.validateInput)
            self.ui.add_instructor_btn.clicked.connect(self.validateInstructorInput)
            self.ui.select_position_comboBox.activated[str].connect(self.get_admin_role)
            self.ui.instructor_status_comboBox.activated[str].connect(self.get_admin_status)
            self.ui.select_instructor_comboBox.activated[str].connect(self.get_instructors)
            self.ui.select_pre_required_comboBox.activated[str].connect(self.get_pre_required_courses)
            self.ui.add_course_btn.clicked.connect(self.validateCourseDetails)
            self.ui.add_entry_test_question_btn.clicked.connect(self.addEntryTestQuestion)
            self.ui.add_section_btn.clicked.connect(self.add_section)
            self.ui.delete_section_btn.clicked.connect(self.deleteSection)
            self.ui.delete_instructor_btn.clicked.connect(self.deleteEmp)
            self.ui.delete_course_btn.clicked.connect(self.deleteCourse)
            self.ui.refresh_instructor_btn.clicked.connect(self.fetchInstructorsRecord)
            self.ui.refresh_courses_btn.clicked.connect(self.fetchCourses)
            self.ui.refresh_entry_test_question_btn.clicked.connect(self.fetchQuestions)
            self.ui.view_std_btn.clicked.connect(self.fetchStudents)
            self.ui.delet_std_btn.clicked.connect(self.deleteStd)
            self.ui.add_std_in_entry_test.clicked.connect(self.addStudentManually)
            self.ui.view_all_entry_test_std_btn.clicked.connect(self.showEntryTestStudents)
            self.ui.view_fee_sdmitted_std_btn.clicked.connect(self.showStudentsPassword)
        except Exception as error:
            print(error)

    # show current login user name on front page

    def showLoginUserName(self):
        try:
            self.user_name = SharedPreferences.user_name.upper()
            self.ui.welcome_label.setText(self.user_name + ", WELCOME TO ADMIN PANEL")
        except Exception as error:
            print(error)

    # panel contain multiple pages using stack widget, so Initialize each page

    def initializePages(self):
        try:
            self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard_page)
        except Exception as error:
            print(error)

    # show dashboard, when user clicks on dashboard option on side menu

    def showDashboard(self):
        try:
            self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard_page)
        except Exception as error:
            print(error)

    # show My Profile, when user clicks on My Profile option on side menu

    def showMyProfile(self):
        try:
            self.ui.stackedWidget.setCurrentWidget(self.ui.my_profile_page)
            self.ui.ID_line_edit.setReadOnly(True)
            self.fetchProfileInfo()
        except Exception as error:
            print(error)

    # show Employees, when user clicks on Employees option on side menu

    def showInstructors(self):
        try:
            self.ui.stackedWidget.setCurrentWidget(self.ui.instructors_page)
            self.fetchInstructorsRecord()
        except Exception as error:
            print(error)

    # show Students, when user clicks on Students option on side menu

    def showStudents(self):
        try:
            self.ui.stackedWidget.setCurrentWidget(self.ui.students_page)
        except Exception as error:
            print(error)

    # show Courses, when user clicks on Courses option on side menu

    def showCourses(self):
        try:
            self.ui.stackedWidget.setCurrentWidget(self.ui.courses_page)
            self.fetchCourses()
            self.ui.select_instructor_comboBox.clear()
            self.ui.select_pre_required_comboBox.clear()
            self.addCoursesToCourseComboBox()
            self.addInstructorsToCourseComboBox()
        except Exception as error:
            print(error)

    # show Question Paper, when user clicks on Question Paper option on side menu

    def showEntryTestPage(self):
        try:
            self.ui.stackedWidget.setCurrentWidget(self.ui.entry_test_page)
            self.fetchQuestionSection()
            self.fetchQuestions()
            self.fetchResult()
        except Exception as error:
            print(error)

    def addStudentManually(self):
        self.ui_add_std_manually = AddStudentForEntryTestWindow()

    def showEntryTestStudents(self):
        self.ui_show_entry_test_students = ShowEntryTestStudentsWindow()

    def showStudentsPassword(self):
        self.ui_show_students_password = ShowStudentsPasswordWindow()

    # Logout

    def logout(self):
        try:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setWindowIcon(QtGui.QIcon(':/Icons/icons/Logo/logo-the-hunar-foundation.jpg'))
            self.msgBox.setText("Do You really want to Logout?")
            self.msgBox.setWindowTitle("Logout")
            self.msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returnValue = self.msgBox.exec()
            if returnValue == QMessageBox.Yes:
                save_info_file = open("save_login_info.txt", "w")
                save_info = [" \n", " \n"]
                save_info_file.writelines(save_info)
                save_info_file.close()
                self.ui = admin_login.LoginWindow()
                self.close()
        except Exception as error:
            print(error)

    def addEntryTestQuestion(self):
        self.add_question_ui = add_question.AddQuestionWindow()

    # Exit

    def exit(self):
        try:
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setWindowIcon(QtGui.QIcon(':/Icons/icons/Logo/logo-the-hunar-foundation.jpg'))
            self.msgBox.setText("Do You really want to Exit?")
            self.msgBox.setWindowTitle("Exit")
            self.msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returnValue = self.msgBox.exec()
            if returnValue == QMessageBox.Yes:
                save_info_file = open("save_login_info.txt", "w")
                save_info = [SharedPreferences.email + "\n", SharedPreferences.admin_password + "\n"]
                save_info_file.writelines(save_info)
                save_info_file.close()
                self.close()
        except Exception as error:
            print(error)

    def validateInput(self):
        try:
            self.admin_name = str(self.ui.name_line_edit.text())
            self.admin_email = str(self.ui.email_lineEdit.text())
            self.admin_contact = str(self.ui.contact_lineEdit.text())
            if self.admin_name == "" or self.admin_email == "" or self.admin_contact == "":
                self.displayErrorMessage()
            else:
                if re.fullmatch(self.emailRegex, self.admin_email) and self.admin_contact.isdigit() and len(
                        self.admin_contact) == 11 and re.fullmatch(self.str_regx, self.admin_name):
                    if self.checkEmailIfAlreadyExist(self.admin_email):
                        self.displayEmailAlreadyExistErrorMessage()
                    else:
                        self.updateMyProfile()
                else:
                    self.displayEmailContactErrorMessage()

        except Exception as error:
            print(error)

    def updateMyProfile(self):
        try:
            conn = createConnection()
            connection = conn.cursor()
            query = '''Update RAASIET_QuizApp.dbo.tbl_admin set admin_full_name=? , admin_email = ? ,
                admin_contact  = ? , admin_profile_updated_on = ? WHERE admin_id=? '''
            connection.execute(query, self.admin_name, self.admin_email, self.admin_contact,
                               self.current_time,
                               SharedPreferences.admin_id)
            conn.commit()
            connection.close()
            self.displayMessageBox("My Profile", "Updated")

        except Exception as error:
            print(error)

    #  ============     Fetching data from Database   ============================

    def fetchProfileInfo(self):
        try:
            conn = createConnection()
            connection = conn.cursor()
            connection.execute(
                "SELECT admin_id,admin_full_name, admin_email,admin_contact,admin_role FROM "
                "RAASIET_QuizApp.dbo.tbl_admin where admin_id = ? ",
                SharedPreferences.admin_id)
            data = connection.fetchone()
            if data is not None:
                self.id = str(data.admin_id)
                self.ui.ID_line_edit.setText(self.id)
                self.ui.name_line_edit.setText(data.admin_full_name)
                self.ui.email_lineEdit.setText(data.admin_email)
                self.ui.contact_lineEdit.setText(data.admin_contact)
            conn.commit()
            connection.close()
        except Exception as error:
            print(error)

    def fetchInstructorsRecord(self):
        try:
            self.ui.show_instructor_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.ui.show_instructor_tableWidget.resizeColumnsToContents()
            query = "SELECT admin_id, admin_full_name, admin_email,admin_contact,admin_role,admin_status  FROM " \
                    "RAASIET_QuizApp.dbo.tbl_admin "
            conn = createConnection()
            connection = conn.cursor()
            cursor = connection.execute(query)
            row_len = []
            for i in cursor:
                row_len.append(len(i))
            if len(row_len) > 0:
                self.col_num = max(row_len)
                self.ui.show_instructor_tableWidget.setRowCount(0)

                cursor = connection.execute(query)
                for row, row_data in enumerate(cursor):
                    self.ui.show_instructor_tableWidget.insertRow(row)
                    for col, col_data in enumerate(row_data):
                        self.ui.show_instructor_tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(col_data)))

                self.ui.show_instructor_tableWidget.resizeColumnsToContents()

            else:
                self.displayMessageBox("Data Not Found", "Currently, You have no Instructors")

            connection.close()

        except Exception as error:
            print(error)

    def fetchCourses(self):
        try:
            self.ui.show_courses_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.ui.show_courses_tableWidget.resizeColumnsToContents()
            query = "SELECT course_id, course_name, course_description, course_fee, course_instructor,course_status, " \
                    "course_active_date, cours_deactive_date, course_added_on," \
                    "course_added_by_name, course_updated_on, course_updated_by_name FROM " \
                    "RAASIET_QuizApp.dbo.tbl_courses "
            conn = createConnection()
            connection = conn.cursor()
            cursor = connection.execute(query)
            row_len = []
            for i in cursor:
                row_len.append(len(i))
            if len(row_len) > 0:
                self.col_num = max(row_len)
                self.ui.show_courses_tableWidget.setRowCount(0)

                cursor = connection.execute(query)
                for row, row_data in enumerate(cursor):
                    self.ui.show_courses_tableWidget.insertRow(row)
                    for col, col_data in enumerate(row_data):
                        self.ui.show_courses_tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(col_data)))

                self.ui.show_courses_tableWidget.resizeColumnsToContents()
            else:
                self.msgBox.setWindowIcon(QtGui.QIcon(':/Icons/icons/Logo/logo-the-hunar-foundation.jpg'))
                self.msgBox.setWindowTitle("Courses")
                self.msgBox.setText("Currently You have no courses")
                self.msgBox.exec_()

        except Exception as error:
            print(error)

    def fetchQuestions(self):
        try:
            self.ui.show_entryTest_paper_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.ui.show_entryTest_paper_tableWidget.resizeColumnsToContents()
            query = "SELECT q_id, question, opt_1_txt,opt_2_txt,opt_3_txt, opt_4_txt, q_right_answer_txt, " \
                    "q_section, q_status, q_added_by_name_admin, q_added_on, q_updated_by_name, " \
                    "q_updated_on FROM " \
                    "RAASIET_QuizApp.dbo.tbl_entry_test_questions "
            conn = createConnection()
            connection = conn.cursor()
            cursor = connection.execute(query)
            row_len = []
            for i in cursor:
                row_len.append(len(i))
            if len(row_len) > 0:
                self.col_num = max(row_len)
                self.ui.show_entryTest_paper_tableWidget.setRowCount(0)

                cursor = connection.execute(query)
                for row, row_data in enumerate(cursor):
                    self.ui.show_entryTest_paper_tableWidget.insertRow(row)
                    for col, col_data in enumerate(row_data):
                        self.ui.show_entryTest_paper_tableWidget.setItem(row, col,
                                                                         QtWidgets.QTableWidgetItem(str(col_data)))

                self.ui.show_entryTest_paper_tableWidget.resizeColumnsToContents()
            else:
                self.displayMessageBox("Question", "Currently, You have no Questions")
        except Exception as error:
            print(error)

    def fetchResult(self):
        try:
            self.ui.view_result_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.ui.view_result_tableWidget.resizeColumnsToContents()
            query = "SELECT std_id_FK, std_name, obt_marks, total_marks, percentage,result_status, result_type, " \
                    "attemp_1_test_date, attemp_2_test_date FROM RAASIET_QuizApp.dbo.tbl_std_result "
            conn = createConnection()
            connection = conn.cursor()
            cursor = connection.execute(query)
            row_len = []
            for i in cursor:
                row_len.append(len(i))
            if len(row_len) > 0:
                self.col_num = max(row_len)
                self.ui.view_result_tableWidget.setRowCount(0)

                cursor = connection.execute(query)
                for row, row_data in enumerate(cursor):
                    self.ui.view_result_tableWidget.insertRow(row)
                    for col, col_data in enumerate(row_data):
                        self.ui.view_result_tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(col_data)))

                self.ui.view_result_tableWidget.resizeColumnsToContents()
            else:
                self.displayMessageBox("Result", "No student has attempt test yet")

        except Exception as error:
            print(error)

    def sendEmailToStudent(self):
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("sender email", "sender email password")
        server.sendmail(
            "sender email",
            "reciever email",
            "body")
        server.quit()


    def fetchStudents(self):
        try:
            self.ui.show_all_std_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.ui.show_all_std_tableWidget.resizeColumnsToContents()
            query = "SELECT ID, Name, Age,contact,Qualification,Institution_Name," \
                    "Email, " \
                    "Course, Gender, Interest, Fees_Status, Date_Added, " \
                    " std_has_attempt_test,test_attempt2_is_allowed, std_updated_by_name, std_updated_on FROM " \
                    "RAASIET_QuizApp.dbo.tbl_entry_test_students"
            conn1 = createConnection()
            connection1 = conn1.cursor()
            cursor = connection1.execute(query)
            row_len = []
            for i in cursor:
                row_len.append(len(i))
            if len(row_len) > 0:
                self.col_num = max(row_len)
                self.ui.show_all_std_tableWidget.setRowCount(0)
                cursor = connection1.execute(query)
                for row, row_data in enumerate(cursor):
                    self.ui.show_all_std_tableWidget.insertRow(row)
                    for col, col_data in enumerate(row_data):
                        self.ui.show_all_std_tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(col_data)))

                self.ui.show_all_std_tableWidget.resizeColumnsToContents()
                conn1.commit()
            else:
                self.displayMessageBox("Students", "Currently, There are no Students")

        except Exception as error:
            print(error)

    # ============  Displaying Error Messages ============================

    def displayEmailContactErrorMessage(self):
        try:
            self.displayMessageBox("Error", "Invalid Email or Contact")

        except Exception as error:
            print(error)

    def checkEmailIfAlreadyExist(self, email):
        try:
            conn = createConnection()
            if conn is not None:
                connection = conn.cursor()
                query = '''Select admin_email From RAASIET_QuizApp.dbo.tbl_admin Where
                                    admin_email=? and admin_id != ?'''
                connection.execute(query, email, SharedPreferences.admin_id)
                data = connection.fetchone()
                conn.commit()
                connection.close()
                if data is not None:
                    return True
                else:
                    return False

        except Exception as error:
            print(error)

    def displayEmailAlreadyExistErrorMessage(self):
        try:
            self.displayMessageBox("Error", "This Email is Already exist")
        except Exception as error:
            print(error)

    def displayErrorMessage(self):
        try:
            self.displayMessageBox("My Profile", "Invalid Input")

        except Exception as error:
            print(error)

    def displayPasswordError(self):
        try:
            self.displayMessageBox("Error", "Password should be 8 characters long")
        except Exception as error:
            print(error)

    # ============================== Add Instructor ==================================
    # get Admin  Role ( Intern or Instructor )

    def get_admin_role(self):
        try:
            self.get_admin_role_txt_combo = self.ui.select_position_comboBox.currentText()
        except Exception as error:
            self.get_admin_role_txt_combo = self.get_admin_role_txt
            print(error)

        # get Admin  Status ( Active or De-active )

    def get_admin_status(self):
        try:
            self.get_admin_status_txt_combo = self.ui.instructor_status_comboBox.currentText()
        except Exception as error:
            self.get_admin_status_txt_combo = self.get_admin_status_txt
            print(error)

    def validateInstructorInput(self):
        try:
            self.instructor_name = str(self.ui.instructor_name_lineEdit.text())
            self.instructor_email = str(self.ui.instructor_email_lineEdit.text())
            self.instructor_contact = str(self.ui.instructor_contact_lineEdit.text())
            self.instructor_password = str(self.ui.instructor_password_lineEdit.text())

            if self.get_admin_role_txt_combo == "":
                self.get_admin_role_txt_combo = self.get_admin_role_txt

            if self.get_admin_status_txt_combo == "":
                self.get_admin_status_txt_combo = self.get_admin_status_txt

            if self.instructor_name == "" or self.instructor_email == "" or self.instructor_contact == "":
                self.displayErrorMessage()

            if len(self.instructor_password) != 8:
                self.displayPasswordError()
            else:
                if re.fullmatch(self.emailRegex, self.instructor_email) and self.instructor_contact.isdigit() and len(
                        self.instructor_contact) == 11 and re.fullmatch(self.str_regx, self.instructor_name):
                    if self.checkEmailIfAlreadyExist(self.instructor_email):
                        self.displayEmailAlreadyExistErrorMessage()
                    else:
                        self.addInstructor()
                else:
                    self.displayEmailContactErrorMessage()

        except Exception as error:
            print(error)

    def addInstructor(self):
        try:
            conn = createConnection()
            connection = conn.cursor()
            query = '''INSERT INTO RAASIET_QuizApp.dbo.tbl_admin (admin_full_name, admin_email,admin_password, 
            admin_contact,admin_role,admin_created_on, admin_status) VALUES(?,?,?,?,?,?,?) '''
            connection.execute(query, self.instructor_name, self.instructor_email, self.instructor_password,
                               self.instructor_contact,
                               self.get_admin_role_txt_combo, self.current_time, self.get_admin_status_txt_combo)
            conn.commit()
            connection.close()
            self.displayMessageBox("Instructor", "Added Successfully")

        except Exception as error:
            print(error)

    def clearInput(self):
        try:
            self.ui.instructor_name_lineEdit.setText("")
            self.ui.instructor_email_lineEdit.setText("")
            self.ui.instructor_password_lineEdit.setText("")
            self.ui.instructor_contact_lineEdit.setText("")

        except Exception as error:
            print(error)

    # ================================== Add Courses ===================================
    def validateCourseDetails(self):
        try:
            self.course_id = str(self.ui.course_ID_lineEdit.text()).upper()
            self.course_name = str(self.ui.course_name_lineEdit.toPlainText())
            self.course_name = self.course_name.lower()
            self.course_desc = str(self.ui.course_description_textEdit.toPlainText())
            self.course_fee = str(self.ui.fee_lineEdit.text())

            self.course_id = self.course_id.replace(" ", "")
            if self.course_name == "" or self.course_id == "":
                self.displayErrorMessage()
                if self.get_course_instructor_txt_combo == "":
                    self.get_course_instructor_txt_combo = "None"
                if self.get_course_preRequired_txt_combo == "":
                    self.get_course_preRequired_txt_combo = "None"
            else:
                self.AddCourse()

        except Exception as error:
            print(error)

    def get_instructors(self):
        try:
            self.get_course_instructor_txt_combo = self.ui.select_instructor_comboBox.currentText()
        except Exception as error:
            self.get_course_instructor_txt_combo = "None"
            print(error)

    def get_pre_required_courses(self):
        try:
            self.get_course_preRequired_txt_combo = self.ui.select_pre_required_comboBox.currentText()
        except Exception as error:
            self.get_course_preRequired_txt_combo = "None"
            print(error)

    def checkIfCourseAlreadyExist(self):
        try:
            conn = createConnection()
            connection = conn.cursor()
            query = '''SELECT course_id from RAASIET_QuizApp.dbo.tbl_courses where course_id = ?'''
            connection.execute(query, self.course_id)
            data = connection.fetchone()
            conn.commit()
            connection.close()
            if data is not None:
                return True
            else:
                return False

        except Exception as error:
            print(error)

    def addCoursesToCourseComboBox(self):
        try:
            conn = createConnection()
            connection = conn.cursor()
            query = '''SELECT course_id from RAASIET_QuizApp.dbo.tbl_courses'''
            connection.execute(query)
            data = connection.fetchall()
            self.courses_list = []
            for x in data:
                self.courses_list.append(x.course_id)
                self.ui.select_pre_required_comboBox.clear()
                self.ui.select_pre_required_comboBox.addItems(self.courses_list)
                print(x.course_id)
            conn.commit()
            connection.close()
            if data is not None:
                return True
            else:
                return False

        except Exception as error:
            print(error)

    def addInstructorsToCourseComboBox(self):
        try:
            conn = createConnection()
            connection = conn.cursor()
            query = '''SELECT admin_full_name from RAASIET_QuizApp.dbo.tbl_admin'''
            connection.execute(query)
            data = connection.fetchall()
            conn.commit()
            connection.close()
            self.admin_list = []
            for x in data:
                self.admin_list.append(x.admin_full_name)
                self.ui.select_instructor_comboBox.clear()
                self.ui.select_instructor_comboBox.addItems(self.admin_list)
                print(x.admin_full_name)

            if data is not None:
                return True
            else:
                return False

        except Exception as error:
            print(error)

    def displayErrorMessageAlreadyExist(self):
        try:
            self.displayMessageBox("Course", "Already Exists")
        except Exception as error:
            print(error)

    def AddCourse(self):
        try:
            if self.checkIfCourseAlreadyExist():
                self.displayErrorMessageAlreadyExist()
            else:
                conn = createConnection()
                connection = conn.cursor()
                query = '''INSERT INTO RAASIET_QuizApp.dbo.tbl_courses (course_id, course_name, course_description, 
                course_fee, course_instructor,course_batch, course_preRequired, course_added_on,course_added_by_name,
                course_added_by, course_status, course_active_date) VALUES(?,?,?,?,?,?,?,?, ?,?,?,?) '''
                connection.execute(query, self.course_id, self.course_name, self.course_desc, self.course_fee,
                                   self.get_course_instructor_txt_combo, "A", self.get_course_preRequired_txt_combo,
                                   self.current_time, SharedPreferences.user_name, SharedPreferences.admin_id,
                                   "Active",
                                   self.current_time)
                conn.commit()
                connection.close()
                self.displayMessageBox("Courses", "Added")

        except Exception as error:
            print(error)

    def clearCourseInput(self):
        try:
            self.ui.course_name_lineEdit.setPlainText("")
            self.ui.course_description_textEdit.setPlainText("")
            self.ui.course_ID_lineEdit.setText("")
            self.ui.fee_lineEdit.setText("")

        except Exception as error:
            print(error)

    # ================================= Add Section ===================================
    def add_section(self):
        try:
            self.section_text = str(self.ui.section_name_lineEdit.text())
            if self.section_text != "":
                self.section_text = self.section_text.lower()
                if self.checkSectionIfAlreadyExist():
                    self.displayMessageBox("Section", "Already Exists")
                else:
                    conn1 = createConnection()
                    connection1 = conn1.cursor()
                    query1 = '''INSERT INTO RAASIET_QuizApp.dbo.q_section (q_sec_text, q_sec_added_on) 
                       VALUES(?,?) '''
                    connection1.execute(query1, self.section_text, self.added_on)
                    conn1.commit()
                    connection1.close()
                    self.displayMessageBox("Section", "Added")
                    self.fetchQuestionSection()
            else:
                self.displayErrorMessage()
        except Exception as error:
            print(error)

    def fetchQuestionSection(self):
        try:
            query = "SELECT q_sec_text FROM RAASIET_QuizApp.dbo.q_section"
            conn = createConnection()
            connection = conn.cursor()
            connection.execute(query)
            rows = connection.fetchall()
            connection.close()
            self.section_list = []
            if rows != None:
                for row in rows:
                    self.section_list.append(row.q_sec_text)
                for data in self.section_list:
                    # Create an item with a caption
                    item = QStandardItem(data)
                    # Add the item to the model
                    self.model.appendRow(item)
                self.ui.show_sections_listView.setModel(self.model)
                # Show the window and run the app
                self.ui.show_sections_listView.show()
            else:
                self.section_list = ["None"]
                self.ui.show_sections_listView.addItems(self.section_list)

        except Exception as error:
            print(error)

    def deleteSection(self):
        try:
            indices = self.ui.show_sections_listView.selectedIndexes()
            # self.section_name = indices.text()
            print(self.section_name)
            try:
                conn = createConnection()
                connection = conn.cursor()
                data = connection.execute("DELETE FROM RAASIET_QuizApp.dbo.q_section WHERE q_sec_text=?",
                                          (self.section_name))
                conn.commit()
                connection.close()
                self.fetchQuestionSection()

            except Exception as error:
                print(error)

        except IndexError:
            self.displayMessageBox("Section", "Please Select a section which you want to delete")

    def checkSectionIfAlreadyExist(self):
        try:
            conn = createConnection()
            if conn is not None:
                connection = conn.cursor()
                query = '''SELECT q_sec_text FROM RAASIET_QuizApp.dbo.q_section Where
                                       q_sec_text=?'''
                connection.execute(query, self.section_text)
                data = connection.fetchone()
                conn.commit()
                connection.close()
                if data is not None:
                    return True
                else:
                    return False

        except Exception as error:
            print(error)

    # ================================== Deletion ======================================
    def deleteEmp(self):
        try:
            firstColValue: QTableWidgetItem = self.ui.show_instructor_tableWidget.selectedItems()[0]
            self.emp_id = firstColValue.text()
            self.emp_id_int = int(self.emp_id)
            if self.emp_id_int != SharedPreferences.admin_id:
                try:
                    if self.checkAdminHasDoneDuty():
                        conn1 = createConnection()
                        connection1 = conn1.cursor()
                        query1 = '''Update RAASIET_QuizApp.dbo.tbl_admin set admin_status=?, admin_profile_updated_on = ? 
                           Where admin_id=? '''
                        connection1.execute(query1, 'de-active', self.current_time, self.emp_id_int)
                        self.displayMessageBox("Instructor", "You can't delete record. Just de-activate account")
                        conn1.commit()
                        connection1.close()
                        self.fetchInstructorsRecord()
                    else:
                        conn = createConnection()
                        connection = conn.cursor()
                        data = connection.execute("DELETE FROM RAASIET_QuizApp.dbo.tbl_admin WHERE admin_id=?",
                                                  (self.emp_id_int))
                        if data is not None:
                            self.displayMessageBox("Instructor", "Deleted")
                            conn.commit()
                            connection.close()
                            self.fetchInstructorsRecord()


                except Exception as error:
                    print(error)


            else:
                self.displayMessageBox("Instructor", "Sorry! you can't delete your own account")
        except IndexError:
            self.displayMessageBox("Instructor", "Please select an instructor to delete record")

    def checkAdminHasDoneDuty(self):
        try:
            conn = createConnection()
            if conn is not None:
                connection = conn.cursor()
                query = '''Select course_added_by From RAASIET_QuizApp.dbo.tbl_courses Where course_added_by=? or 
                course_update_by=? '''
                connection.execute(query, self.emp_id_int, self.emp_id_int)
                data = connection.fetchone()
                conn.commit()
                if data is not None:
                    return True
                else:
                    conn = createConnection()
                    connection = conn.cursor()
                    query = '''Select q_added_by_admin_id_FK From RAASIET_QuizApp.dbo.tbl_entry_test_questions Where 
                    q_added_by_admin_id_FK=? or q_updated_by =? '''
                    connection.execute(query, self.emp_id_int, self.emp_id_int)
                    data = connection.fetchone()
                    conn.commit()
                    if data is not None:
                        return True
                    else:
                        return False

        except Exception as error:
            print(error)

    def checkIfStudentsAreRegistered(self):
        try:
            return True
        except Exception as error:
            print(error)

    def deleteCourse(self):
        try:
            firstColValue: QTableWidgetItem = self.ui.show_courses_tableWidget.selectedItems()[0]
            self.course_id = firstColValue.text()
            # self.course_id_int = int(self.course_id)
            try:
                # add one more if here to check whether course has quizzes or not
                if self.checkIfStudentsAreRegistered():
                    conn1 = createConnection()
                    connection1 = conn1.cursor()
                    query1 = '''Update RAASIET_QuizApp.dbo.tbl_courses set course_status=?, cours_deactive_date= ?, 
                    course_updated_on =?, course_updated_by_name = ?, course_update_by = ? Where course_id=? '''
                    connection1.execute(query1, 'de-active', self.current_time, self.current_time,
                                        SharedPreferences.user_name, SharedPreferences.admin_id, self.course_id)
                    conn1.commit()
                    connection1.close()
                    self.displayMessageBox("Courses", "Course de-activated")
                    self.fetchCourses()

                else:
                    conn = createConnection()
                    connection = conn.cursor()
                    data = connection.execute("DELETE FROM RAASIET_QuizApp.dbo.tbl_courses WHERE course_id=?",
                                              (self.course_id))
                    if data is not None:
                        self.displayMessageBox("Courses", "'Deleted")
                        conn.commit()
                        connection.close()
                        self.fetchCourses()

            except Exception as error:
                print(error)


        except IndexError:
            self.displayMessageBox("Courses", "Please select a course you want to delete")

    def deleteStd(self):
        try:
            firstColValue: QTableWidgetItem = self.ui.show_all_std_tableWidget.selectedItems()[0]
            self.std_id = firstColValue.text()
            self.std_id_int = int(self.std_id)
            try:
                if self.checkIfStudentHasSubmitFee():
                    self.displayMessageBox("Deletion Error","Student has submit the fee. His/Her record can't be "
                                                            "deleted")
                else:
                    if self.checkIfStudentHasAttemptTest():
                        self.msgBox.setIcon(QMessageBox.Information)
                        self.msgBox.setWindowIcon(QtGui.QIcon(':/Icons/icons/Logo/logo-the-hunar-foundation.jpg'))
                        self.msgBox.setText(
                            "This student has attempt the test? Do you really want to delete this student? Remember If "
                            "you delete this, All records of this student will be deleted")
                        self.msgBox.setWindowTitle("Delete")
                        self.msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                        returnValue = self.msgBox.exec()
                        if returnValue == QMessageBox.Yes:
                            self.deleteOtherRecords()
                            conn3 = createConnection()
                            connection3 = conn3.cursor()
                            connection3.execute("DELETE FROM RAASIET_QuizApp.dbo.tbl_entry_test_students WHERE ID=?", (self.std_id_int))
                            conn3.commit()
                            self.successDeleteStudent()

                    else:
                        conn = createConnection()
                        connection = conn.cursor()
                        data = connection.execute("DELETE FROM RAASIET_QuizApp.dbo.tbl_entry_test_students WHERE ID=?", (self.std_id_int))
                        conn.commit()
                        self.successDeleteStudent()

            except Exception as error:
                print(error)

        except IndexError:
            self.displayMessageBox("Error", "Please Select a student which you want to delete")

    def checkIfStudentHasAttemptTest(self):
        try:
            conn = createConnection()
            if conn is not None:
                connection = conn.cursor()
                query = '''Select std_id_FK From RAASIET_QuizApp.dbo.tbl_std_result Where std_id_FK = ?'''
                connection.execute(query, self.std_id_int)
                data = connection.fetchone()
                conn.commit()
                if data is not None:
                    return True
                else:
                    return False
        except Exception as error:
            print(error)

    def checkIfStudentHasSubmitFee(self):
        try:
            conn = createConnection()
            if conn is not None:
                connection = conn.cursor()
                query = '''Select ID From RAASIET_QuizApp.dbo.tbl_entry_test_students Where ID = ? and Fees_Status = 
                'Initiated' '''
                connection.execute(query, self.std_id_int)
                data = connection.fetchone()
                conn.commit()
                if data is not None:
                    return True
                else:
                    return False
        except Exception as error:
            print(error)

    def deleteOtherRecords(self):
        try:
            conn1 = createConnection()
            connection1 = conn1.cursor()
            connection1.execute("DELETE FROM RAASIET_QuizApp.dbo.tbl_std_result WHERE std_id_FK=?", (self.std_id_int))
            conn1.commit()

            conn2 = createConnection()
            connection2 = conn2.cursor()
            connection2.execute("DELETE FROM RAASIET_QuizApp.dbo.tbl_std_answers WHERE std_id_FK=?", (self.std_id_int))
            conn2.commit()

        except Exception as error:
            print(error)

    def successDeleteStudent(self):
        try:
            self.displayMessageBox("Student", "Deleted")
            self.ui.show_all_std_tableWidget.setRowCount(0)
            self.fetchStudents()

        except Exception as error:
            print(error)

    # ================================== Add Student for Entry Test Exam ===================
    def read_and_modify_csv(self):
        self.launchDialog()
        if self.FilePath != "":
            self.test_attempt2_is_allowed = "No"
            self.std_has_attempt_test = "No"
            # Opening the person-records.csv file
            file = open(self.FilePath)
            self.df = pd.read_csv(file)
            self.df.sort_values(["ID"], axis=0, ascending=[True], inplace=True)
            self.df = self.df.fillna('None')
            self.df = self.df.rename(columns=({'Institution Name': 'Institution_Name'}))
            self.df = self.df.rename(columns=({'Fees Status': 'Fees_Status'}))
            self.df = self.df.rename(columns=({'Date Added': 'Date_Added'}))
            self.df = self.df.astype({'ID': int, 'Age': int}, errors='ignore')
            #self.df = self.df.astype({'Age': int}, errors='ignore')
            self.df["Date_Added"] = self.df["Date_Added"].astype('datetime64', errors='ignore')
            self.df['Name'] = self.df['Name'].str.title()
            self.df['Course'] = self.df['Course'].str.lower()
            self.df['Institution_Name'] = self.df['Institution_Name'].str.upper()
            self.df['Qualification'] = self.df['Qualification'].str.upper()
            self.df['Email'] = self.df['Email'].str.lower()

            return True
        else:
            self.displayMessageBox("File Error", "No File Selected")

    def logic(self):
        logic_conn = createConnection()
        logic_connection = logic_conn.cursor()
        try:
            query = '''INSERT INTO RAASIET_QuizApp.dbo.tbl_entry_test_students(ID, Name, Age, contact, Qualification, 
              Institution_Name,Email,Course,Gender,Interest,Fees_Status, Date_Added, test_attempt2_is_allowed, 
              std_has_attempt_test) VALUES(?,?,?,?,?,?, ?,?,?,?,?,?,?,?) '''
            for index, row in self.df.iterrows():
                logic_connection.execute(query, row.ID, row.Name, row.Age,
                                         row.contact, row.Qualification, row.Institution_Name,
                                         row.Email, row.Course, row.Gender,
                                         row.Interest, row.Fees_Status, row.Date_Added,
                                         self.test_attempt2_is_allowed, self.std_has_attempt_test)
            logic_conn.commit()
            logic_connection.close()

        except Exception as error:
            logic_conn.commit()
            logic_connection.close()
            self.insert_in_temp_table()

    def insert_in_temp_table(self):
        try:
            conn1 = createConnection()
            connection1 = conn1.cursor()
            # Insert Dataframe into SQL Server:
            query1 = '''INSERT INTO RAASIET_QuizApp.dbo.tbl_entry_test_students_temp(ID, Name, Age, contact, Qualification, 
                                      Institution_Name,Email,Course,Gender,Interest,Fees_Status, Date_Added, test_attempt2_is_allowed, 
                                      std_has_attempt_test) VALUES(?,?,?,?,?,?, ?,?,?,?,?,?,?,?) '''
            for index, row in self.df.iterrows():
                connection1.execute(query1, row.ID, row.Name, row.Age,
                                    row.contact, row.Qualification, row.Institution_Name,
                                    row.Email, row.Course, row.Gender,
                                    row.Interest, row.Fees_Status, row.Date_Added,
                                    self.test_attempt2_is_allowed, self.std_has_attempt_test)
            conn1.commit()
            connection1.close()
            self.update_records()

        except Exception as error:
            self.delete_records()

    def update_records(self):
        try:
            conn2 = createConnection()
            connection2 = conn2.cursor()
            query2 = '''Update RAASIET_QuizApp.dbo.tbl_entry_test_students set
              RAASIET_QuizApp.dbo.tbl_entry_test_students.Name = t.Name,
              RAASIET_QuizApp.dbo.tbl_entry_test_students.Age = t.Age,
              RAASIET_QuizApp.dbo.tbl_entry_test_students.contact = t.contact, 
              RAASIET_QuizApp.dbo.tbl_entry_test_students.Qualification = t.Qualification,
              RAASIET_QuizApp.dbo.tbl_entry_test_students.Institution_Name = t.Institution_Name,
              RAASIET_QuizApp.dbo.tbl_entry_test_students.Email = t.Email ,
              RAASIET_QuizApp.dbo.tbl_entry_test_students.Course= t.Course,
              RAASIET_QuizApp.dbo.tbl_entry_test_students.Gender = t.Gender,
              RAASIET_QuizApp.dbo.tbl_entry_test_students.Interest = t.Interest,
              RAASIET_QuizApp.dbo.tbl_entry_test_students.Fees_Status= t.Fees_Status , 
              RAASIET_QuizApp.dbo.tbl_entry_test_students.Date_Added = t.Date_Added,
              RAASIET_QuizApp.dbo.tbl_entry_test_students.test_attempt2_is_allowed = t.test_attempt2_is_allowed,
              RAASIET_QuizApp.dbo.tbl_entry_test_students.std_has_attempt_test = t.std_has_attempt_test
              FROM RAASIET_QuizApp.dbo.tbl_entry_test_students c INNER JOIN 
              RAASIET_QuizApp.dbo.tbl_entry_test_students_temp t on 
              t.ID = c.ID and t.Fees_Status = '-' '''

            connection2.execute(query2)
            conn2.commit()
            connection2.close()

        except Exception as error:
            print(error)

    def delete_records(self):
        try:
            delete_records_con = createConnection()
            cursorConnection = delete_records_con.cursor()
            query3 = '''delete from RAASIET_QuizApp.dbo.tbl_entry_test_students_temp'''
            cursorConnection.execute(query3)
            delete_records_con.commit()
            cursorConnection.close()

        except Exception as error:
            print(error)

    def upload_csv(self):
        if self.read_and_modify_csv():
            self.delete_records()
            self.logic()
            self.createPasswords()
            self.delete_records()

    def launchDialog(self):
        try:
            self.FilePath = self.getFileName()

        except Exception as error:
            print(error)
            self.FilePath = ""

    def getFileName(self):
        try:
            file_filter = 'CSV File (*.csv)'
            response = QFileDialog.getOpenFileName(
                parent=None,
                caption='Select a CSV File',
                directory=os.getcwd(),
                filter=file_filter,
                initialFilter='CSV File (*.csv)'
            )
            return response[0]

        except Exception as error:
            print(error)

    def createPasswords(self):
        password_conn = createConnection()
        password_connection = password_conn.cursor()
        query3 = '''SELECT ID, Name, Course, contact, Email from RAASIET_QuizApp.dbo.tbl_entry_test_students where 
        Fees_Status = 'Initiated' '''
        password_connection.execute(query3)
        data = password_connection.fetchall()
        password_conn.commit()
        password_connection.close()
        if data is not None:
            for row in data:
                password_conn2 = createConnection()
                connection4 = password_conn2.cursor()
                query4 = '''SELECT course_id, course_batch from RAASIET_QuizApp.dbo.tbl_courses where course_name = ?'''
                connection4.execute(query4, row[2])
                data1 = connection4.fetchone()
                if data1 is not None:
                    self.course_id_new = data1.course_id
                    self.course_batch = data1.course_batch

                password_conn2.commit()
                connection4.close()
                value = str(row[0])
                current_year = datetime.today().year
                current_year = str(current_year)[-2:]
                self.password = self.course_id_new + "-" + current_year + "-" + self.course_batch + "-" + value
                conn5 = createConnection()
                connection5 = conn5.cursor()
                try:
                    query5 = '''INSERT INTO RAASIET_QuizApp.dbo.entry_test_students_id_pass (ID, Name, course_ID, 
                    course_batch, std_password, std_contact, std_email) VALUES (?,?,?,?,?,?,?)'''
                    connection5.execute(query5, row[0], row[1], self.course_id_new, self.course_batch, self.password,
                                        row[3], row[4])
                    conn5.commit()
                    connection5.close()
                    self.alterPasswordTable()
                except Exception as error:
                    conn5.commit()
                    connection5.close()

    def alterPasswordTable(self):
        conn = createConnection()
        connection = conn.cursor()
        try:
            connection.execute("DELETE FROM RAASIET_QuizApp.dbo.entry_test_students_id_pass WHERE ID NOT IN(SELECT "
                               "MIN(ID) AS 'ID' FROM "
                               "entry_test_students_id_pass GROUP BY course_ID, std_contact) ")
            conn.commit()
            connection.close()
        except Exception as error:
            conn.commit()

    # ================================== Display Message Box ===========================

    def displayMessageBox(self, title, message):
        self.msg = QMessageBox()
        self.msg.setWindowIcon(QtGui.QIcon(':/Icons/icons/Logo/logo-the-hunar-foundation.jpg'))
        self.msg.setWindowTitle(title)
        self.msg.setText(message)
        self.msg.exec_()
        self.clearInput()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminPanelWindow()
    sys.exit(app.exec_())
