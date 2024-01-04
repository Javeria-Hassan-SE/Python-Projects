# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import gspread
import win32com.client
import requests
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

global data

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]
def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data
def WMIDateStringToDate(dtmDate):
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
def Info():
    strComputer = "."
    data = []
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    objSWbemServices = objWMIService.ConnectServer(strComputer, "root\cimv2")
    colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_BIOS")
    for objItem in colItems:
        print("BiosCharacteristics:")
        strList = " "
        try:
            for objElem in objItem.BiosCharacteristics:
                strList = strList + objElem + ","
        except:
            strList = strList + 'null'
        print(strList)
        data.append(strList)
        print("BIOSVersion:")
        strList = " "
        try:
            for objElem in objItem.BIOSVersion:
                strList = strList + objElem + ","
        except:
            strList = strList + 'null'
        print(strList)
        data.append(strList)
        # if objItem.BuildNumber is not None:
        #     data.append(objItem.BuildNumber)
        #     print("BuildNumber:" + objItem.BuildNumber)
        if objItem.Caption is not None:
            data.append(objItem.Caption)
            print("Caption:" + objItem.Caption)
        # if objItem.CodeSet is not None:
        #     data.append(objItem.CodeSet)
        #     print("CodeSet:" + objItem.CodeSet)
        if objItem.CurrentLanguage is not None:
            data.append(objItem.CurrentLanguage)
            print("CurrentLanguage:" + objItem.CurrentLanguage)
        if objItem.Description is not None:
            data.append(objItem.Description)
            print("Description:" + objItem.Description)
        # if objItem.IdentificationCode is not None:
        #     data.append(objItem.IdentificationCode)
        #     print("IdentificationCode:" + objItem.IdentificationCode)
        if objItem.InstallableLanguages is not None:
            data.append(objItem.InstallableLanguages)
            print("InstallableLanguages:", objItem.InstallableLanguages)
        # if objItem.InstallDate is not None:
        #     data.append(WMIDateStringToDate(objItem.InstallDate))
        #     print("InstallDate:" + WMIDateStringToDate(objItem.InstallDate))
        # if objItem.LanguageEdition is not None:
        #     data.append(objItem.LanguageEdition)
        #     print("LanguageEdition:" + objItem.LanguageEdition)
        print("ListOfLanguages:")
        strList = " "
        try:
            for objElem in objItem.ListOfLanguages:
                strList = strList + objElem + ","
        except:
            strList = strList + 'null'
        print(strList)
        data.append(strList)
        if objItem.Manufacturer is not None:
            print("Manufacturer:" + objItem.Manufacturer)
        data.append(objItem.Manufacturer)
        if objItem.Name is not None:
            print("Name:" + objItem.Name)
        data.append(objItem.Name)
        # if objItem.OtherTargetOS is not None:
        #     print("OtherTargetOS:" + objItem.OtherTargetOS)
        # data.append(objItem.OtherTargetOS)
        if objItem.PrimaryBIOS is not None:
            print("PrimaryBIOS:", objItem.PrimaryBIOS)
        data.append(objItem.PrimaryBIOS)
        if objItem.ReleaseDate is not None:
            print("ReleaseDate:" + WMIDateStringToDate(objItem.ReleaseDate))
            data.append(WMIDateStringToDate(objItem.ReleaseDate))
        if objItem.SerialNumber is not None:
            print("SerialNumber:" + objItem.SerialNumber)
        data.append(objItem.SerialNumber)
        if objItem.SMBIOSBIOSVersion is not None:
            print("SMBIOSBIOSVersion:" + objItem.SMBIOSBIOSVersion)
        data.append(objItem.SMBIOSBIOSVersion)
        if objItem.SMBIOSMajorVersion is not None:
            print("SMBIOSMajorVersion:", objItem.SMBIOSMajorVersion)
        data.append(objItem.SMBIOSMajorVersion)
        if objItem.SMBIOSMinorVersion is not None:
            print("SMBIOSMinorVersion:", objItem.SMBIOSMinorVersion)
        data.append(objItem.SMBIOSMinorVersion)
        if objItem.SMBIOSPresent is not None:
            print("SMBIOSPresent:", objItem.SMBIOSPresent)
        data.append(objItem.SMBIOSPresent)
        if objItem.SoftwareElementID is not None:
            print("SoftwareElementID:" + objItem.SoftwareElementID)
        data.append(objItem.SoftwareElementID)
        if objItem.SoftwareElementState is not None:
            print("SoftwareElementState:", objItem.SoftwareElementState)
        data.append(objItem.SoftwareElementState)
        if objItem.Status is not None:
            print("Status:" + objItem.Status)
        data.append(objItem.Status)
        if objItem.TargetOperatingSystem is not None:
            print("TargetOperatingSystem:", objItem.TargetOperatingSystem)
        data.append(objItem.TargetOperatingSystem)
        if objItem.Version is not None:
            print("Version:" + objItem.Version)
        else:
            print("No value")
        data.append(objItem.Version)
        print(data)
        sa = gspread.service_account(filename="https://drive.google.com/file/d/1OBYTLcG2dblIQ6Hu03nYAaFiOm0pOKSQ/view?usp=sharing")
        sh = sa.open("GoogleAPI")

        wks = sh.worksheet("Sheet1")

        print('Rows: ', wks.row_count)
        print('Cols: ', wks.col_count)

        # print(wks.acell('A9').value)
        # print(wks.cell(3, 4).value)
        print(wks.get('A7:E9'))

        # to get all records
        print(wks.get_all_records())

        # to get all values
        print(wks.get_all_values())

        # wks.update('A3', 'Anthony')
        # wks.update('D2:E3', [['Engineering', 'Tennis'], ['Business', 'Pottery']])
        # wks.update('F2', '=UPPER(E2)', raw=False)

        gauth = GoogleAuth()
        drive = GoogleDrive(gauth)
        wks.delete_rows(25)
        wks.insert_row(data, 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    Info()
    print("Location: ", get_location())
    input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
