from PyQt5.QtWidgets import *
import sys
from database_connection import *
from PyQt5 import QtWidgets, QtGui, QtCore
from UI_show_entry_test_students import Ui_EntryTestStudentsWindow


class ShowEntryTestStudentsWindow(QMainWindow):
    def __init__(self):
        try:
            QMainWindow.__init__(self)
            self.ui = Ui_EntryTestStudentsWindow()
            self.ui.setupUi(self)
            self.fetchStudents()
            self.show()
        except Exception as error:
            print(error)

    def fetchStudents(self):
        try:
            self.ui.show_entry_test_students_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.ui.show_entry_test_students_tableWidget.resizeColumnsToContents()
            query = "SELECT ID, Name, Age,contact,Qualification,Institution_Name," \
                    "Email, " \
                    "Course, Gender, Interest, Fees_Status, Date_Added, " \
                    " std_has_attempt_test,test_attempt2_is_allowed FROM " \
                    "RAASIET_QuizApp.dbo.tbl_entry_test_students"
            conn1 = createConnection()
            connection1 = conn1.cursor()
            cursor = connection1.execute(query)
            row_len = []
            for i in cursor:
                row_len.append(len(i))
            if len(row_len) > 0:
                self.col_num = max(row_len)
                self.ui.show_entry_test_students_tableWidget.setRowCount(0)
                cursor = connection1.execute(query)
                for row, row_data in enumerate(cursor):
                    self.ui.show_entry_test_students_tableWidget.insertRow(row)
                    for col, col_data in enumerate(row_data):
                        self.ui.show_entry_test_students_tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(col_data)))

                self.ui.show_entry_test_students_tableWidget.resizeColumnsToContents()
                conn1.commit()
            else:
                self.displayMessageBox("Students", "Currently, There are no Students")

        except Exception as error:
            print(error)

    def displayMessageBox(self, title, message):
        self.msg = QMessageBox()
        self.msg.setWindowIcon(QtGui.QIcon(':/Icons/icons/Logo/logo-the-hunar-foundation.jpg'))
        self.msg.setWindowTitle(title)
        self.msg.setText(message)
        self.msg.exec_()
        self.clearInput()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShowEntryTestStudentsWindow()
    sys.exit(app.exec_())
