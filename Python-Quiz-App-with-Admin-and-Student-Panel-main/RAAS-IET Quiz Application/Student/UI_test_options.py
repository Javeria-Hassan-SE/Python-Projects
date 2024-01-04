# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_options.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChooseOptions(object):
    def setupUi(self, ChooseOptions):
        ChooseOptions.setObjectName("ChooseOptions")
        ChooseOptions.resize(1024, 644)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/backgrounds/hands.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChooseOptions.setWindowIcon(icon)
        ChooseOptions.setStyleSheet("QFrame#test_options_form{\n"
"background-color: rgb(48, 78, 151);\n"
"border-radius:40px;\n"
"margin: 60px;\n"
"}\n"
"QFrame#border_frame\n"
"{\n"
"background-color:#6fa844 ;\n"
"}\n"
"QFrame#main_frame{\n"
"background-image: url(:/icons/Background2.jpg);\n"
"\n"
"background-position:center;\n"
"background-repeat:no-repeat;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(ChooseOptions)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.border_frame)
        self.verticalLayout_2.setContentsMargins(80, 80, 80, 80)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.heading_side_bar = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heading_side_bar.sizePolicy().hasHeightForWidth())
        self.heading_side_bar.setSizePolicy(sizePolicy)
        self.heading_side_bar.setMinimumSize(QtCore.QSize(240, 0))
        self.heading_side_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.heading_side_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.heading_side_bar.setLineWidth(0)
        self.heading_side_bar.setObjectName("heading_side_bar")
        self.RAAS_heading_label = QtWidgets.QLabel(self.heading_side_bar)
        self.RAAS_heading_label.setGeometry(QtCore.QRect(10, 10, 121, 41))
        self.RAAS_heading_label.setStyleSheet("color: rgb(48, 78, 151);\n"
"font: 63 32pt \"Bahnschrift SemiBold\";")
        self.RAAS_heading_label.setObjectName("RAAS_heading_label")
        self.ET_label = QtWidgets.QLabel(self.heading_side_bar)
        self.ET_label.setGeometry(QtCore.QRect(10, 60, 221, 101))
        self.ET_label.setStyleSheet("color: rgb(48, 78, 151);\n"
"font: 25 22pt \"Bahnschrift Light\";")
        self.ET_label.setWordWrap(True)
        self.ET_label.setObjectName("ET_label")
        self.horizontalLayout.addWidget(self.heading_side_bar)
        self.test_options_form = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_options_form.sizePolicy().hasHeightForWidth())
        self.test_options_form.setSizePolicy(sizePolicy)
        self.test_options_form.setMinimumSize(QtCore.QSize(470, 480))
        self.test_options_form.setMaximumSize(QtCore.QSize(16777215, 800))
        self.test_options_form.setStyleSheet("")
        self.test_options_form.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test_options_form.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.test_options_form.setLineWidth(0)
        self.test_options_form.setObjectName("test_options_form")
        self.class_test_btn = QtWidgets.QPushButton(self.test_options_form)
        self.class_test_btn.setGeometry(QtCore.QRect(110, 310, 250, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.class_test_btn.sizePolicy().hasHeightForWidth())
        self.class_test_btn.setSizePolicy(sizePolicy)
        self.class_test_btn.setMinimumSize(QtCore.QSize(250, 40))
        self.class_test_btn.setMaximumSize(QtCore.QSize(100, 40))
        self.class_test_btn.setStyleSheet("background-color: rgb(111, 168, 68);\n"
"border-radius: 15px;\n"
"color: rgb(241, 241, 241);\n"
"font:  bold 10pt \"Bahnschrift Light\";margin:5px;\n"
"vertical-align: center;\n"
"horizontal-align: center;")
        self.class_test_btn.setAutoDefault(False)
        self.class_test_btn.setFlat(False)
        self.class_test_btn.setObjectName("class_test_btn")
        self.entry_test_btn = QtWidgets.QPushButton(self.test_options_form)
        self.entry_test_btn.setGeometry(QtCore.QRect(110, 250, 250, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_test_btn.sizePolicy().hasHeightForWidth())
        self.entry_test_btn.setSizePolicy(sizePolicy)
        self.entry_test_btn.setMinimumSize(QtCore.QSize(250, 40))
        self.entry_test_btn.setMaximumSize(QtCore.QSize(100, 40))
        self.entry_test_btn.setStyleSheet("background-color: rgb(111, 168, 68);\n"
"border-radius: 15px;\n"
"color: rgb(241, 241, 241);\n"
"font:  bold 10pt \"Bahnschrift Light\";margin:5px;\n"
"vertical-align: center;\n"
"horizontal-align: center;")
        self.entry_test_btn.setAutoDefault(False)
        self.entry_test_btn.setFlat(False)
        self.entry_test_btn.setObjectName("entry_test_btn")
        self.choose_your_test_label = QtWidgets.QLabel(self.test_options_form)
        self.choose_your_test_label.setGeometry(QtCore.QRect(110, 180, 239, 39))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_your_test_label.sizePolicy().hasHeightForWidth())
        self.choose_your_test_label.setSizePolicy(sizePolicy)
        self.choose_your_test_label.setStyleSheet("color: rgb(241, 241, 241);\n"
"\n"
"font: 25 18pt \"Bahnschrift Light Condensed\";\n"
"margin:5px;")
        self.choose_your_test_label.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_your_test_label.setObjectName("choose_your_test_label")
        self.welcome_heading = QtWidgets.QLabel(self.test_options_form)
        self.welcome_heading.setGeometry(QtCore.QRect(80, 70, 311, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome_heading.sizePolicy().hasHeightForWidth())
        self.welcome_heading.setSizePolicy(sizePolicy)
        self.welcome_heading.setStyleSheet("color: rgb(241, 241, 241);\n"
"font: 63 20pt \"Bahnschrift SemiBold\";\n"
"margin:5px;")
        self.welcome_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_heading.setWordWrap(True)
        self.welcome_heading.setObjectName("welcome_heading")
        self.error_label = QtWidgets.QLabel(self.test_options_form)
        self.error_label.setEnabled(True)
        self.error_label.setGeometry(QtCore.QRect(140, 380, 200, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy)
        self.error_label.setMinimumSize(QtCore.QSize(200, 0))
        self.error_label.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 25 12pt \"Bahnschrift Light\";\n"
"margin:5px;")
        self.error_label.setText("")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.horizontalLayout.addWidget(self.test_options_form, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.logo_side_bar = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_side_bar.sizePolicy().hasHeightForWidth())
        self.logo_side_bar.setSizePolicy(sizePolicy)
        self.logo_side_bar.setMinimumSize(QtCore.QSize(150, 0))
        self.logo_side_bar.setStyleSheet("")
        self.logo_side_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_side_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_side_bar.setLineWidth(0)
        self.logo_side_bar.setObjectName("logo_side_bar")
        self.gridLayout = QtWidgets.QGridLayout(self.logo_side_bar)
        self.gridLayout.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.hunar_logo = QtWidgets.QLabel(self.logo_side_bar)
        self.hunar_logo.setMinimumSize(QtCore.QSize(80, 120))
        self.hunar_logo.setMaximumSize(QtCore.QSize(80, 120))
        self.hunar_logo.setStyleSheet("background-image: url(:/icons/icons/backgrounds/Asset 7-100.jpg);\n"
"background-repeat: no-repeat; \n"
" background-position: right;\n"
"margin:5px;\n"
"")
        self.hunar_logo.setText("")
        self.hunar_logo.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.hunar_logo.setObjectName("hunar_logo")
        self.gridLayout.addWidget(self.hunar_logo, 0, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.logo_side_bar)
        self.verticalLayout_2.addWidget(self.main_frame)
        self.verticalLayout.addWidget(self.border_frame)
        ChooseOptions.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChooseOptions)
        QtCore.QMetaObject.connectSlotsByName(ChooseOptions)

    def retranslateUi(self, ChooseOptions):
        _translate = QtCore.QCoreApplication.translate
        ChooseOptions.setWindowTitle(_translate("ChooseOptions", "MainWindow"))
        self.RAAS_heading_label.setText(_translate("ChooseOptions", "RAAS"))
        self.ET_label.setText(_translate("ChooseOptions", "INSTITUTE OF EMERGING TECHNOLOGIES"))
        self.class_test_btn.setText(_translate("ChooseOptions", "CLASS TEST"))
        self.entry_test_btn.setText(_translate("ChooseOptions", "ENTRY TEST"))
        self.choose_your_test_label.setText(_translate("ChooseOptions", "Select your Test"))
        self.welcome_heading.setText(_translate("ChooseOptions", "WELCOME TO THE TEST PORTAL"))
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChooseOptions = QtWidgets.QMainWindow()
    ui = Ui_ChooseOptions()
    ui.setupUi(ChooseOptions)
    ChooseOptions.show()
    sys.exit(app.exec_())