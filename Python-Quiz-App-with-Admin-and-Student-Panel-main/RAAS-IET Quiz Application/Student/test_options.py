from UI_test_options import Ui_ChooseOptions
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from instructions import *
from student_portal import *


class TestOptionsWindow(QMainWindow):
    def __init__(self):
        try:
            QMainWindow.__init__(self, parent=None)
            self.ui = Ui_ChooseOptions()
            self.ui.setupUi(self)
            self.show()
            self.btnClicked()
        except Exception as error:
            print(error)

    def btnClicked(self):
        self.ui.entry_test_btn.clicked.connect(self.showInstructionsPanel)
        self.ui.class_test_btn.clicked.connect(self.showStudentPortal)

    def showInstructionsPanel(self):
        try:
            self.ui_instructions = InstructionsWindow()
            self.close()
        except Exception as error:
            print(error)


    def showStudentPortal(self):
        try:
            self.ui_studentPortal = StudentPortalWindow()
            self.close()
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestOptionsWindow()
    sys.exit(app.exec_())
