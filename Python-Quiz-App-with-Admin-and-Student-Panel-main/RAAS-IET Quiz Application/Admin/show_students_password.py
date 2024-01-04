from PyQt5.QtWidgets import *
import sys
from UI_show_students_password import Ui_StudentsPasswordWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from database_connection import *


class ShowStudentsPasswordWindow(QMainWindow):
    def __init__(self):
        try:
            QMainWindow.__init__(self)
            self.ui = Ui_StudentsPasswordWindow()
            self.ui.setupUi(self)
            self.fetchPasswordStudentData()
            self.show()
        except Exception as error:
            print(error)

    def fetchPasswordStudentData(self):
        try:
            self.ui.show_students_password_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.ui.show_students_password_tableWidget.resizeColumnsToContents()
            query = "SELECT ID, Name, course_ID,course_batch, std_password,std_contact," \
                    "std_email FROM " \
                    "RAASIET_QuizApp.dbo.entry_test_students_id_pass"
            conn1 = createConnection()
            connection1 = conn1.cursor()
            cursor = connection1.execute(query)
            row_len = []
            for i in cursor:
                row_len.append(len(i))
            if len(row_len) > 0:
                self.col_num = max(row_len)
                self.ui.show_students_password_tableWidget.setRowCount(0)
                cursor = connection1.execute(query)
                for row, row_data in enumerate(cursor):
                    self.ui.show_students_password_tableWidget.insertRow(row)
                    for col, col_data in enumerate(row_data):
                        self.ui.show_students_password_tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(col_data)))

                self.ui.show_students_password_tableWidget.resizeColumnsToContents()
                self.ui.show_students_password_tableWidget.sortItems(0, QtCore.Qt.AscendingOrder)
                conn1.commit()
            else:
                self.msgBox.setWindowIcon(QtGui.QIcon(':/Icons/icons/Logo/logo-the-hunar-foundation.jpg'))
                self.msgBox.setWindowTitle("Students")
                self.msgBox.setText("No Student registered yet")
                self.msgBox.exec_()

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
    window = ShowStudentsPasswordWindow()
    sys.exit(app.exec_())
