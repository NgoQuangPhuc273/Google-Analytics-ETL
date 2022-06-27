import sys

sys.path.insert(0, 'ETL/User_Info')
sys.path.insert(0, 'ETL/Page_Info')
sys.path.insert(0, 'ETL/Store_Info')
sys.path.insert(0, 'ETL/Session_Info')


from datetime import datetime
import User_General_ETL
import User_General_toSQLServer
import User_Detailed_ETL
import User_Detailed_toSQLServer
import PageETL
import PagetoSQLServer
import StoreETL
import StoretoSQLServer
import SessionETL
import SessiontoSQLServer

def user_general_info():
    #Get User data from Google Analytics to local 
    try:
        User_General_ETL.main()
        User_General_toSQLServer.load()

        print("Successfully Extract, Tranform and Load User_General_Info!")

    except:
        print("An error has occurred in User_General_Info.")

def user_detailed_info():
    #Get User data from Google Analytics to local 
    try:
        User_Detailed_ETL.main()
        User_Detailed_toSQLServer.load()

        print("Successfully Extract, Tranform and Load User_Detailed_Info!")

    except:
        print("An error has occurred in User_Detailed_Info.")

def page_info():
    #Get Page data from Google Analytics to local 
    try:
        PageETL.main()
        PagetoSQLServer.load()

        print("Successfully Extract, Tranform and Load Page_Info!")

    except:
        print("An error has occurred in Page_Info.")

def store_info():
    #Get Page data from Google Analytics to local 
    try:
        StoreETL.main()
        StoretoSQLServer.load()

        print("Successfully Extract, Tranform and Load Store_Info!")

    except:
        print("An error has occurred in Store_Info.")

def session_info():
    try:
        SessionETL.main()
        SessiontoSQLServer.load()

        print("Successfully Extract, Tranform and Load Session_Info!")

    except:
        print("An error has occurred in Session_Info.")

if __name__ == '__main__':
    print(datetime.now())
    print("")

    user_general_info()
    user_detailed_info()
    page_info()
    store_info()
    session_info()
    
