# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_entry_test_students.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EntryTestStudentsWindow(object):
    def setupUi(self, EntryTestStudentsWindow):
        EntryTestStudentsWindow.setObjectName("EntryTestStudentsWindow")
        EntryTestStudentsWindow.resize(1024, 644)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/backgrounds/hands.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EntryTestStudentsWindow.setWindowIcon(icon)
        EntryTestStudentsWindow.setStyleSheet("QFrame#login_form{\n"
"background-color: rgb(48, 78, 151);\n"
"border-radius:40px;\n"
"margin: 60px;\n"
"}\n"
"QFrame#border_frame\n"
"{\n"
"background-color:#6fa844 ;\n"
"}\n"
"QFrame#main_frame{\n"
"background-image: url(:/icons/icons/backgrounds/Background.jpg);\n"
"\n"
"background-position:center;\n"
"background-repeat:no-repeat;\n"
"}\n"
"QComboBox#search_filter_comboBox::down-arrow\n"
"{\n"
"color :green;\n"
"}\n"
"QPushButton::ToolTip\n"
"{\n"
"background-color: white;\n"
"color:black;\n"
"background-image:none;\n"
"}\n"
"QTabWidget{background: gray;}")
        self.centralwidget = QtWidgets.QWidget(EntryTestStudentsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.border_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.border_frame.sizePolicy().hasHeightForWidth())
        self.border_frame.setSizePolicy(sizePolicy)
        self.border_frame.setStyleSheet("")
        self.border_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.border_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.border_frame.setObjectName("border_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.border_frame)
        self.gridLayout_6.setContentsMargins(40, 40, 40, 40)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.main_frame = QtWidgets.QFrame(self.border_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.main_frame.setStyleSheet("")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.header_frame = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setMinimumSize(QtCore.QSize(0, 120))
        self.header_frame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.header_frame.setStyleSheet("")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.header_gridLayout = QtWidgets.QGridLayout()
        self.header_gridLayout.setSpacing(0)
        self.header_gridLayout.setObjectName("header_gridLayout")
        self.hunar_logo = QtWidgets.QLabel(self.header_frame)
        self.hunar_logo.setMinimumSize(QtCore.QSize(70, 100))
        self.hunar_logo.setMaximumSize(QtCore.QSize(70, 100))
        self.hunar_logo.setStyleSheet("\n"
"background-image: url(:/icons/icons/backgrounds/Asset 7-100.jpg);\n"
"background-repeat: no-repeat; \n"
" background-position: right;\n"
"margin:5px;\n"
"")
        self.hunar_logo.setText("")
        self.hunar_logo.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.hunar_logo.setObjectName("hunar_logo")
        self.header_gridLayout.addWidget(self.hunar_logo, 0, 0, 2, 1)
        self.ET_label = QtWidgets.QLabel(self.header_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ET_label.sizePolicy().hasHeightForWidth())
        self.ET_label.setSizePolicy(sizePolicy)
        self.ET_label.setMinimumSize(QtCore.QSize(541, 0))
        self.ET_label.setStyleSheet("color: rgb(48, 78, 151);\n"
"font: 25 22pt \"Bahnschrift Light\";")
        self.ET_label.setWordWrap(True)
        self.ET_label.setObjectName("ET_label")
        self.header_gridLayout.addWidget(self.ET_label, 1, 1, 1, 1)
        self.RAAS_label = QtWidgets.QLabel(self.header_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RAAS_label.sizePolicy().hasHeightForWidth())
        self.RAAS_label.setSizePolicy(sizePolicy)
        self.RAAS_label.setMinimumSize(QtCore.QSize(120, 0))
        self.RAAS_label.setStyleSheet("color: rgb(48, 78, 151);\n"
"font: 63 32pt \"Bahnschrift SemiBold\";")
        self.RAAS_label.setObjectName("RAAS_label")
        self.header_gridLayout.addWidget(self.RAAS_label, 0, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.header_gridLayout)
        self.verticalLayout_3.addWidget(self.header_frame)
        self.frame = QtWidgets.QFrame(self.main_frame)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.center_label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.center_label.sizePolicy().hasHeightForWidth())
        self.center_label.setSizePolicy(sizePolicy)
        self.center_label.setMinimumSize(QtCore.QSize(541, 0))
        self.center_label.setStyleSheet("color: rgb(48, 78, 151);\n"
"font: 18pt \"Bahnschrift Ligh\";")
        self.center_label.setAlignment(QtCore.Qt.AlignCenter)
        self.center_label.setWordWrap(True)
        self.center_label.setObjectName("center_label")
        self.horizontalLayout_4.addWidget(self.center_label)
        self.verticalLayout_3.addWidget(self.frame)
        self.main_body = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setMinimumSize(QtCore.QSize(0, 0))
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.show_entry_test_students_tableWidget = QtWidgets.QTableWidget(self.main_body)
        self.show_entry_test_students_tableWidget.setStyleSheet("font: 12pt \"Bahnschrift Ligh\";")
        self.show_entry_test_students_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.show_entry_test_students_tableWidget.setObjectName("show_entry_test_students_tableWidget")
        self.show_entry_test_students_tableWidget.setColumnCount(14)
        self.show_entry_test_students_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.show_entry_test_students_tableWidget.setHorizontalHeaderItem(13, item)
        self.show_entry_test_students_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.horizontalLayout.addWidget(self.show_entry_test_students_tableWidget)
        self.verticalLayout_3.addWidget(self.main_body)
        self.gridLayout_6.addWidget(self.main_frame, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.border_frame)
        EntryTestStudentsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EntryTestStudentsWindow)
        QtCore.QMetaObject.connectSlotsByName(EntryTestStudentsWindow)

    def retranslateUi(self, EntryTestStudentsWindow):
        _translate = QtCore.QCoreApplication.translate
        EntryTestStudentsWindow.setWindowTitle(_translate("EntryTestStudentsWindow", "MainWindow"))
        self.ET_label.setText(_translate("EntryTestStudentsWindow", "INSTITUTE OF EMERGING TECHNOLOGIES"))
        self.RAAS_label.setText(_translate("EntryTestStudentsWindow", "RAAS"))
        self.center_label.setText(_translate("EntryTestStudentsWindow", "ENTRY TEST STUDENTS"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("EntryTestStudentsWindow", "ID"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("EntryTestStudentsWindow", "Name"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("EntryTestStudentsWindow", "Age"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("EntryTestStudentsWindow", "Contact"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("EntryTestStudentsWindow", "Qualification"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("EntryTestStudentsWindow", "Institution Name"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("EntryTestStudentsWindow", "Email"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("EntryTestStudentsWindow", "Course"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("EntryTestStudentsWindow", "Gender"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("EntryTestStudentsWindow", "Interest"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("EntryTestStudentsWindow", "Fee Status"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("EntryTestStudentsWindow", "Date Added"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("EntryTestStudentsWindow", "Attempt Test?"))
        item = self.show_entry_test_students_tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("EntryTestStudentsWindow", "Is Attempt 2 allowed?"))
import icon_rc