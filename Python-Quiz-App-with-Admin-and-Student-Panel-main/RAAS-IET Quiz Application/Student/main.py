from student_login import *


class MainWindow(QMainWindow):
    def __init__(self):
        try:
            QMainWindow.__init__(self)
            self.ui = StudentLoginWindow()
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
