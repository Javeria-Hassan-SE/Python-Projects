from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys
from UI_add_student_manually import Ui_MainWindow
from database_connection import *
from datetime import datetime
import re


class AddStudentForEntryTestWindow(QMainWindow):
    def __init__(self):
        try:
            QMainWindow.__init__(self)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.current_time = datetime.now()
            self.addCoursesToCourseComboBox()
            self.combo_course = ""
            self.combo_fee = ""
            self.combo_gender = ""
            self.interest = "None"
            self.emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|org|edu.pk|edu.com|com.pk)+\b'
            self.str_regx = r'\b[A-Za-z ]+'
            self.getID()
            self.ui.std_chosen_course_comboBox.activated[str].connect(self.get_course)
            self.ui.std_gender_comboBox.activated[str].connect(self.get_gender)
            self.ui.std_feeStatus_comboBox.activated[str].connect(self.get_feeStatus)
            self.ui.addStudent_btn.clicked.connect(self.validateData)
            self.show()
        except Exception as error:
            print(error)

    def get_course(self):
        try:
            self.combo_course = self.ui.std_chosen_course_comboBox.currentText()
        except Exception as error:
            self.combo_course = self.combo_course
            print(error)

    def get_gender(self):
        try:
            self.combo_gender = self.ui.std_gender_comboBox.currentText()
        except Exception as error:
            self.combo_gender = self.combo_gender
            print(error)

    def get_feeStatus(self):
        try:
            self.combo_fee = self.ui.std_feeStatus_comboBox.currentText()
        except Exception as error:
            self.combo_fee = self.combo_fee
            print(error)

    def addCoursesToCourseComboBox(self):
        try:
            conn1 = createConnection()
            connection1 = conn1.cursor()
            query = '''SELECT course_name from RAASIET_QuizApp.dbo.tbl_courses'''
            connection1.execute(query)
            data = connection1.fetchall()
            self.courses_list = []
            for x in data:
                self.courses_list.append(x.course_name)
                self.ui.std_chosen_course_comboBox.clear()
                self.ui.std_chosen_course_comboBox.addItems(self.courses_list)
            conn1.commit()
            connection1.close()
            if data is not None:
                return True
            else:
                return False

        except Exception as error:
            print(error)

    def getID(self):
        conn2 = createConnection()
        connection2 = conn2.cursor()
        connection2.execute("SELECT TOP 1 ID FROM RAASIET_QuizApp.dbo.tbl_entry_test_students ORDER BY ID DESC")
        data = connection2.fetchone()
        self.studentID = data.ID + 1
        conn2.commit()
        connection2.close()


    def validateData(self):
        self.student_name =str(self.ui.student_name_lineEdit.text()).title()
        self.student_contact =str(self.ui.student_contact_lineEdit.text())
        self.student_email =str(self.ui.std_email_lineEdit.text()).lower()
        self.student_qualification =str(self.ui.std_qualification_lineEdit.text()).upper()
        self.student_institute_name =str(self.ui.std_instituitionName_lineEdit.text()).upper()
        self.student_age =str(self.ui.std_age_spinBox.value())
        self.student_course =self.combo_course
        self.fee_status =self.combo_fee
        self.student_interest =str(self.ui.std_interest_comboBox.text())
        self.student_gender=self.combo_gender

        if self.student_name == "" or self.student_contact == "" or self.student_email == "" or self.student_qualification == "" or self.student_institute_name == "" or self.student_age == "" or self.student_course == "" or self.fee_status == "" or self.student_gender == "" :
            self.displayMessageBox("Error", "Please fill all data")
        else:
            if re.fullmatch(self.emailRegex, self.student_email) and self.student_contact.isdigit() and len(
                    self.student_contact) == 11 and re.fullmatch(self.str_regx, self.student_name):
                        if self.checkIfAlreadyRegistered():
                            self.displayMessageBox("Error", "You are already registered in this course")
                        else:
                            self.AddStudent()

    def checkIfAlreadyRegistered(self):
        try:
            conn3 = createConnection()
            if conn3 is not None:
                connection3 = conn3.cursor()
                query = '''Select contact, Course From RAASIET_QuizApp.dbo.tbl_entry_test_students Where
                                           contact = ? and Course = ?'''
                connection3.execute(query, self.student_contact, self.student_course)
                data = connection3.fetchone()
                conn3.commit()
                connection3.close()
                if data is not None:
                    return True
                else:
                    return False

        except Exception as error:
            print(error)

    def AddStudent(self):
        try:
            conn4 = createConnection()
            connection4 = conn4.cursor()
            query = '''INSERT INTO RAASIET_QuizApp.dbo.tbl_entry_test_students(ID, Name, Age, contact, Qualification, 
                             Institution_Name,Email,Course,Gender,Interest,Fees_Status, Date_Added, test_attempt2_is_allowed, 
                             std_has_attempt_test) VALUES(?,?,?,?,?,?, ?,?,?,?,?,?,?,?) '''
            connection4.execute(query, self.studentID , self.student_name,self.student_age, self.student_contact,self.student_qualification,
                                   self.student_institute_name,self.student_email,
                                   self.student_course ,self.student_gender,self.student_interest,self.fee_status, self.current_time,
                                   "No",
                                   "No")
            conn4.commit()
            connection4.close()
            self.createPasswords()
            self.displayMessageBox("Student", "Added")

        except Exception as error:
            print(error)

    def createPasswords(self):
        if self.fee_status == "Initiated":
            password_conn = createConnection()
            connection5 = password_conn.cursor()
            query4 = '''SELECT course_id, course_batch from RAASIET_QuizApp.dbo.tbl_courses where course_name = ?'''
            connection5.execute(query4, self.student_course)
            data1 = connection5.fetchone()
            if data1 is not None:
                self.course_id_new = data1.course_id
                self.course_batch = data1.course_batch

            password_conn.commit()
            connection5.close()
            value = str(self.studentID)
            current_year = datetime.today().year
            current_year = str(current_year)[-2:]
            self.password = self.course_id_new + "-" + current_year + "-" + self.course_batch + "-" + value
            conn6 = createConnection()
            connection6 = conn6.cursor()
            try:
                query5 = '''INSERT INTO RAASIET_QuizApp.dbo.entry_test_students_id_pass (ID, Name, course_ID, 
                course_batch, std_password, std_contact, std_email) VALUES (?,?,?,?,?,?,?)'''
                connection6.execute(query5, value, self.student_name, self.course_id_new, self.course_batch, self.password,
                                        self.student_contact, self.student_email)
                conn6.commit()
                connection6.close()
            except Exception as error:
                conn6.commit()
                connection6.close()
        else:
            print("no password created because fee is not submitted")

    def displayMessageBox(self, title, message):
        self.msg = QMessageBox()
        self.msg.setWindowIcon(QtGui.QIcon(':/Icons/icons/Logo/logo-the-hunar-foundation.jpg'))
        self.msg.setWindowTitle(title)
        self.msg.setText(message)
        self.msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddStudentForEntryTestWindow()
    sys.exit(app.exec_())
