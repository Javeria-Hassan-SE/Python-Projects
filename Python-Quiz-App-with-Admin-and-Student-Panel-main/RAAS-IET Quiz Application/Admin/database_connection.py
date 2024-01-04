import pyodbc


def createConnection():
    try:
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=DESKTOP-O32G07C\SQLEXPRESS;'
                              'Database=RAASIET_QuizApp;'
                              'Trusted_Connection=yes;')
        return conn
    except Exception as error:
        print(error)
