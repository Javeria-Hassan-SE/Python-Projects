from admin_login import *
from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        try:
            QMainWindow.__init__(self)
            self.ui = LoginWindow()
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
