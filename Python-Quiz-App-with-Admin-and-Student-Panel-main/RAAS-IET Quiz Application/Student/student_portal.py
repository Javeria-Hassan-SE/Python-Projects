from UI_student_portal import Ui_StudentPortal
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from instructions import *


class StudentPortalWindow(QMainWindow):
    def __init__(self):
        try:
            QMainWindow.__init__(self, parent=None)
            self.ui = Ui_StudentPortal()
            self.ui.setupUi(self)
            self.show()
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentPortalWindow()
    sys.exit(app.exec_())
