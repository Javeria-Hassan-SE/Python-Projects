# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import win32com.client
import requests
import time
import sys

from urllib3.connectionpool import xrange


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
        print("BIOSVersion:")
        strList = " "
        try:
            for objElem in objItem.BIOSVersion:
                strList = strList + objElem + ","
        except:
            strList = strList + 'null'
        print(strList)
        if objItem.BuildNumber is not None:
            print("BuildNumber:" + objItem.BuildNumber)
        if objItem.Caption is not None:
            print("Caption:" + objItem.Caption)
        if objItem.CodeSet is not None:
            print("CodeSet:" + objItem.CodeSet)
        if objItem.CurrentLanguage is not None:
            print("CurrentLanguage:" + objItem.CurrentLanguage)
        if objItem.Description is not None:
            print("Description:" + objItem.Description)
        if objItem.IdentificationCode is not None:
            print("IdentificationCode:" + objItem.IdentificationCode)
        if objItem.InstallableLanguages is not None:
            print("InstallableLanguages:", objItem.InstallableLanguages)
        if objItem.InstallDate is not None:
            print("InstallDate:" + WMIDateStringToDate(objItem.InstallDate))
        if objItem.LanguageEdition is not None:
            print("LanguageEdition:" + objItem.LanguageEdition)
        print("ListOfLanguages:")
        strList = " "
        try:
            for objElem in objItem.ListOfLanguages:
                strList = strList + objElem + ","
        except:
            strList = strList + 'null'
        print(strList)
        if objItem.Manufacturer is not None:
            print("Manufacturer:" + objItem.Manufacturer)
        if objItem.Name is not None:
            print("Name:" + objItem.Name)
        if objItem.OtherTargetOS is not None:
            print("OtherTargetOS:" + objItem.OtherTargetOS)
        if objItem.PrimaryBIOS is not None:
            print("PrimaryBIOS:", objItem.PrimaryBIOS)
        if objItem.ReleaseDate is not None:
            print("ReleaseDate:" + WMIDateStringToDate(objItem.ReleaseDate))
        if objItem.SerialNumber is not None:
            print("SerialNumber:" + objItem.SerialNumber)
        if objItem.SMBIOSBIOSVersion is not None:
            print("SMBIOSBIOSVersion:" + objItem.SMBIOSBIOSVersion)
        if objItem.SMBIOSMajorVersion is not None:
            print("SMBIOSMajorVersion:", objItem.SMBIOSMajorVersion)
        if objItem.SMBIOSMinorVersion is not None:
            print("SMBIOSMinorVersion:", objItem.SMBIOSMinorVersion)
        if objItem.SMBIOSPresent is not None:
            print("SMBIOSPresent:", objItem.SMBIOSPresent)
        if objItem.SoftwareElementID is not None:
            print("SoftwareElementID:" + objItem.SoftwareElementID)
        if objItem.SoftwareElementState is not None:
            print("SoftwareElementState:", objItem.SoftwareElementState)
        if objItem.Status is not None:
            print("Status:" + objItem.Status)
        if objItem.TargetOperatingSystem is not None:
            print("TargetOperatingSystem:", objItem.TargetOperatingSystem)
        if objItem.Version is not None:
            print("Version:" + objItem.Version)
        else:
            print("No value")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Info()
    print("Location: ", get_location())
    toolbar_width = 40

    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['

    for i in xrange(toolbar_width):
        time.sleep(0.1)  # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("]\n")  # this ends the progress bar

    input()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
