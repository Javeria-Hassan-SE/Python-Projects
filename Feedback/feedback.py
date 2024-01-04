import ctypes
import re
import sys
import os
from PyQt5.QtWidgets import *
from ui_feedback import *
import requests
import win32com.client
from datetime import datetime
import gspread


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]
    except Exception as error:
        print(error)


def WMIDateStringToDate(dtmDate):
    try:
        if dtmDate[4] == 0:
            strDateTime = dtmDate[5] + '/'
        else:
            strDateTime = dtmDate[4] + dtmDate[5] + '/'
        if dtmDate[6] == 0:
            strDateTime = strDateTime + dtmDate[7] + '/'
        else:
            strDateTime = strDateTime + dtmDate[6] + dtmDate[7] + '/'
            strDateTime = strDateTime + dtmDate[0] + dtmDate[1] + dtmDate[2] + dtmDate[3] + " " + dtmDate[8] + dtmDate[
                9] + ":" + dtmDate[10] + dtmDate[11] + ':' + dtmDate[12] + dtmDate[13]
        return strDateTime
    except Exception as error:
        print(error)


class Feedback(QMainWindow):

    # UI Initialization

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.studentFeedBack = "None"
        self.studentEmail = "None"
        self.studentName = "None"
        self.instructorName = "Not Selected"
        self.instituteName = "THF"
        self.courseName = "Not Selected"
        self.emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|org|edu.pk|edu.com|com.pk|yahoo.com)+\b'
        self.str_regx = r'\b[A-Za-z ]+'
        self.ip = "none"
        self.city = "none"
        self.country = "none"
        self.region = "none"
        self.shift = "Not Selected"
        self.answer1 = "Not Selected"
        self.answer2 = "Not Selected"
        self.answer3 = "Not Selected"
        self.answer4 = "Not Selected"
        self.answer5 = "Not Selected"
        self.answer6 = "Not Selected"
        self.answer7 = "Not Selected"
        self.answer8 = "Not Selected"
        self.error = "None"
        self.strComputer = "."
        self.biosCharacteristics = "None"
        self.biosVersion = "None"
        self.Caption = "None"
        self.currentLanguage = "None"
        self.description = "None"
        self.InstallableLanguages = "None"
        self.listOfLanguages = "None"
        self.manufacturer = "None"
        self.name = "None"
        self.primaryBIOS = "None"
        self.releaseDate = "None"
        self.serialNumber = "None"
        self.SMBIOSVersion = "None"
        self.SMBIOSMajorVersion = "None"
        self.SMBIOSMinorVersion = "None"
        self.SMBIOSPresent = "None"
        self.SoftwareElementID = "None"
        self.softwareElementState = "None"
        self.status = "None"
        self.targetOperatingSystem = "None"
        self.version = "None"
        self.now = datetime.now()
        self.currentDateTime = self.now.strftime("%d/%m/%Y %H:%M:%S")
        self.service = gspread.service_account(filename=resource_path("pytogsheets-358505-07ea97ee0197.json"))
        self.workbook = self.service.open("GoogleAPI")
        self.workSheet = self.workbook.worksheet("FeedbackInfo")
        self.data = []
        self.btnClicked()

    def btnClicked(self):
        try:
            self.ui.submitPushButton.clicked.connect(self.validateInput)
            self.ui.instructorComboBox.activated[str].connect(self.getInstructorName)
            self.ui.institueComboBox.activated[str].connect(self.getInstituteName)
            self.ui.courseComboBox.activated[str].connect(self.getCourseName)
        except Exception as error:
            print(error)

    def getInstructorName(self):
        try:
            self.instructorName = self.ui.instructorComboBox.currentText()
        except Exception:
            self.instructorName = self.instructorName

    def getInstituteName(self):
        try:
            self.instituteName = self.ui.institueComboBox.currentText()
        except Exception as error:
            self.instituteName = self.instituteName
            print(error)

    def getCourseName(self):
        try:
            self.courseName = self.ui.courseComboBox.currentText()
        except Exception as error:
            self.courseName = self.courseName
            print(error)

    def getUserInput(self):
        self.studentName = str(self.ui.nameLineEdit.text()).title()
        self.studentEmail = str(self.ui.emailLineEdit.text()).lower()
        self.studentFeedBack = str(self.ui.feedbackPlainTextEdit.toPlainText()).title()

    def getRadioButtonInput(self):
        try:
            if self.ui.morningRadioButton.isChecked():
                self.shift = "Morning"
            if self.ui.afternoonRadioButton.isChecked():
                self.shift = "Afternoon"
            if self.ui.q1YesRB.isChecked():
                self.answer1 = "Yes"
            if self.ui.q2YesRB.isChecked():
                self.answer2 = "Yes"
            if self.ui.q3YesRB.isChecked():
                self.answer3 = "Yes"
            if self.ui.q4YesRB.isChecked():
                self.answer4 = "Yes"
            if self.ui.q5YesRB.isChecked():
                self.answer5 = "Yes"
            if self.ui.q6YesRB.isChecked():
                self.answer6 = "Yes"
            if self.ui.q7YesRB.isChecked():
                self.answer7 = "Yes"
            if self.ui.q8YesRB.isChecked():
                self.answer8 = "Yes"
            if self.ui.q1NoRB.isChecked():
                self.answer1 = "No"
            if self.ui.q2NoRB.isChecked():
                self.answer2 = "No"
            if self.ui.q3NoRB.isChecked():
                self.answer3 = "No"
            if self.ui.q4NoRB.isChecked():
                self.answer4 = "No"
            if self.ui.q5NoRB.isChecked():
                self.answer5 = "No"
            if self.ui.q6NoRB.isChecked():
                self.answer6 = "No"
            if self.ui.q7NoRB.isChecked():
                self.answer7 = "No"
            if self.ui.q8NoRB.isChecked():
                self.answer8 = "No"
        except Exception as error:
            self.error = error

    def validateInput(self):
        self.ui.submitPushButton.setText("Submitting....")
        try:
            self.getUserInput()
            self.getRadioButtonInput()
            if self.studentName == "" or self.studentEmail == "" or self.studentFeedBack == "" \
                    or self.instructorName == "Not Selected" or self.courseName == "Not Selected" \
                    or self.shift == "Not Selected" \
                    or self.answer1 == "Not Selected" or self.answer2 == "Not Selected" \
                    or self.answer3 == "Not Selected" or self.answer4 == "Not Selected" \
                    or self.answer5 == "Not Selected" or self.answer6 == "Not Selected" \
                    or self.answer7 == "Not Selected" or self.answer8 == "Not Selected":
                self.displayMessageBox("Error", "Please provide all Information")
            else:
                if re.fullmatch(self.emailRegex, self.studentEmail) and re.fullmatch(self.str_regx, self.studentName):
                    self.getLocationInformation()
                    self.getBiosInformation()
                    self.addToGoogleSheets()
                    self.ui.submitPushButton.setDisabled(True)
                    self.displayMessageBox("NAVTTC Portal", "Thankyou for your response")
                    self.data.clear()
                    self.close()
                else:
                    self.displayMessageBox("Invalid Input", "Invalid Name or Email")
        except Exception as error:
            self.error = error

    def getLocationInformation(self):
        try:
            ip_address = get_ip()
            response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
            location_data = {
                "ip": ip_address,
                "city": response.get("city"),
                "region": response.get("region"),
                "country": response.get("country_name")
            }
            self.ip = location_data["ip"]
            self.city = location_data["city"]
            self.region = location_data["region"]
            self.country = location_data["country"]
        except Exception as error:
            self.error = error

    def getBiosInformation(self):
        try:
            objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
            objSWbemServices = objWMIService.ConnectServer(self.strComputer, "root\cimv2")
            colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_BIOS")
            for objItem in colItems:
                self.biosCharacteristics = "None"
                try:
                    for objElem in objItem.BiosCharacteristics:
                        self.biosCharacteristics = self.biosCharacteristics + objElem + ","
                except:
                    self.biosCharacteristics = self.biosCharacteristics + 'null'
                self.biosVersion = " "
                try:
                    for objElem in objItem.BIOSVersion:
                        self.biosVersion = self.biosVersion + objElem + ","
                except:
                    self.biosVersion = self.biosVersion + 'None'
                if objItem.Caption is not None:
                    self.Caption = objItem.Caption
                else:
                    self.Caption = self.Caption + " null"
                if objItem.CurrentLanguage is not None:
                    self.currentLanguage = objItem.CurrentLanguage
                else:
                    self.currentLanguage = self.currentLanguage + "null"
                if objItem.Description is not None:
                    self.description = objItem.Description
                else:
                    self.description = self.description + "null"
                if objItem.InstallableLanguages is not None:
                    self.InstallableLanguages = objItem.InstallableLanguages
                else:
                    self.InstallableLanguages = self.InstallableLanguages + "null"
                self.listOfLanguages = " "
                try:
                    for objElem in objItem.ListOfLanguages:
                        self.listOfLanguages = self.listOfLanguages + objElem + ","
                except:
                    self.listOfLanguages = self.listOfLanguages + 'null'
                if objItem.Manufacturer is not None:
                    self.manufacturer = objItem.Manufacturer
                else:
                    self.manufacturer = self.manufacturer + 'null'
                if objItem.Name is not None:
                    self.name = objItem.Name
                else:
                    self.name = self.name + "null"
                if objItem.PrimaryBIOS is not None:
                    self.primaryBIOS = objItem.PrimaryBIOS
                else:
                    self.primaryBIOS = self.primaryBIOS + "null"
                if objItem.ReleaseDate is not None:
                    self.releaseDate = WMIDateStringToDate(objItem.ReleaseDate)
                else:
                    self.releaseDate = self.releaseDate + "null"
                if objItem.SerialNumber is not None:
                    self.serialNumber = objItem.SerialNumber
                else:
                    self.serialNumber = self.serialNumber + "null"
                if objItem.SMBIOSBIOSVersion is not None:
                    self.SMBIOSVersion = objItem.SMBIOSBIOSVersion
                else:
                    self.SMBIOSVersion = self.SMBIOSVersion + "null"
                if objItem.SMBIOSMajorVersion is not None:
                    self.SMBIOSMajorVersion = objItem.SMBIOSMajorVersion
                else:
                    self.SMBIOSMajorVersion = self.SMBIOSMajorVersion + "null"
                if objItem.SMBIOSMinorVersion is not None:
                    self.SMBIOSMinorVersion = objItem.SMBIOSMinorVersion
                else:
                    self.SMBIOSMinorVersion = self.SMBIOSMinorVersion + "null"
                if objItem.SMBIOSPresent is not None:
                    self.SMBIOSPresent = objItem.SMBIOSPresent
                else:
                    self.SMBIOSPresent = self.SMBIOSPresent + "null"
                if objItem.SoftwareElementID is not None:
                    self.SoftwareElementID = objItem.SoftwareElementID
                else:
                    self.SoftwareElementID = self.SoftwareElementID + "null"
                if objItem.SoftwareElementState is not None:
                    self.softwareElementState = objItem.SoftwareElementState
                else:
                    self.softwareElementState = self.softwareElementState + "null"
                if objItem.Status is not None:
                    self.status = objItem.Status
                else:
                    self.status = self.status + "null"
                if objItem.TargetOperatingSystem is not None:
                    self.targetOperatingSystem = objItem.TargetOperatingSystem
                else:
                    self.targetOperatingSystem = self.targetOperatingSystem + "null"
                if objItem.Version is not None:
                    self.version = objItem.Version
                else:
                    self.version = self.version + "null"
        except Exception as error:
            self.error = error

    def addToGoogleSheets(self):
        try:
            self.addData()
            self.workSheet.insert_row(self.data, 2)
        except Exception as error:
            self.error = error

    def addData(self):
        try:
            self.data.append(self.currentDateTime)
            self.data.append(self.studentName)
            self.data.append(self.studentEmail)
            self.data.append(self.instructorName)
            self.data.append(self.courseName)
            self.data.append(self.instituteName)
            self.data.append(self.shift)
            self.data.append(self.answer1)
            self.data.append(self.answer2)
            self.data.append(self.answer3)
            self.data.append(self.answer4)
            self.data.append(self.answer5)
            self.data.append(self.answer6)
            self.data.append(self.answer7)
            self.data.append(self.answer8)
            self.data.append(self.studentFeedBack)
            self.data.append(self.ip)
            self.data.append(self.city)
            self.data.append(self.region)
            self.data.append(self.country)
            self.data.append(self.biosCharacteristics)
            self.data.append(self.biosVersion)
            self.data.append(self.Caption)
            self.data.append(self.currentLanguage)
            self.data.append(self.description)
            self.data.append(self.InstallableLanguages)
            self.data.append(self.listOfLanguages)
            self.data.append(self.manufacturer)
            self.data.append(self.name)
            self.data.append(self.primaryBIOS)
            self.data.append(self.releaseDate)
            self.data.append(self.serialNumber)
            self.data.append(self.SMBIOSVersion)
            self.data.append(self.SMBIOSMajorVersion)
            self.data.append(self.SMBIOSMinorVersion)
            self.data.append(self.SMBIOSPresent)
            self.data.append(self.SoftwareElementID)
            self.data.append(self.softwareElementState)
            self.data.append(self.status)
            self.data.append(self.targetOperatingSystem)
            self.data.append(self.version)
        except Exception as error:
            self.error = error

    def displayMessageBox(self, title, message):
        try:
            self.msg = QMessageBox()
            self.msg.setWindowIcon(QtGui.QIcon('navttc-logo.png'))
            self.msg.setWindowTitle(title)
            self.msg.setText(message)
            self.msg.exec_()
        except Exception as error:
            self.error = error



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app.setWindowIcon(QtGui.QIcon(resource_path('navttc-logo.png')))
    window = Feedback()
    sys.exit(app.exec_())
    input()
