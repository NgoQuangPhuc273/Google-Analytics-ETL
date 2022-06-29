import sys

sys.path.insert(0, 'ETL/User_Info')
sys.path.insert(0, 'ETL/Page_Info')
sys.path.insert(0, 'ETL/Store_Info')
sys.path.insert(0, 'ETL/Session_Info')
sys.path.insert(0, 'ETL/Platform_Device_Info')
sys.path.insert(0, 'ETL/Geography_Info')

from datetime import datetime
import User_General_ETL
import User_General_toSQLServer
import User_Detailed_ETL
import User_Detailed_toSQLServer
import UserIDtoSQLServer
import GeoETL
import GeotoSQLServer
import PageETL
import PagetoSQLServer
import PlatformDeviceETL
import PlatformDevicetoSQLServer
import StoreETL
import StoretoSQLServer
import SessionETL
import SessiontoSQLServer

def user_info():
    #Get User data from Google Analytics to local 
    try:
        User_General_ETL.main()
        User_General_toSQLServer.load()

        print("Successfully Extract, Tranform and Load User_General_Info!")

    except:
        print("An error has occurred in User_General_Info.")

    try:
        User_Detailed_ETL.main()
        User_Detailed_toSQLServer.load()

        print("Successfully Extract, Tranform and Load User_Detailed_Info!")

    except:
        print("An error has occurred in User_Detailed_Info.")

    try:
        UserIDtoSQLServer.load()

        print("Successfully Extract, Tranform and Load UserID!")

    except:
        print("An error has occurred in UserID.")


def geography_info():
    try: 
        GeoETL.main()
        GeotoSQLServer.load()

        print("\nSuccessfully Extract, Tranform and Load Geography_info!")

    except:
        print("\nAn error has occurred in Geography_info.")

def page_info():
    #Get Page data from Google Analytics to local 
    try:
        PageETL.main()
        PagetoSQLServer.load()

        print("\nSuccessfully Extract, Tranform and Load Page_Info!")

    except:
        print("\nAn error has occurred in Page_Info.")


def platform_device_info():
    try:
        PlatformDeviceETL.main()
        PlatformDevicetoSQLServer.load()

        print("\nSuccessfully Extract, Tranform and Load Platform_Device_info!")

    except:
        print("\nAn error has occurred in Platform_Device_info.")


def store_info():
    #Get Page data from Google Analytics to local 
    try:
        StoreETL.main()
        StoretoSQLServer.load()

        print("\nSuccessfully Extract, Tranform and Load Store_Info!")

    except:
        print("\nAn error has occurred in Store_Info.")

def session_info():
    try:
        SessionETL.main()
        SessiontoSQLServer.load()

        print("\nSuccessfully Extract, Tranform and Load Session_Info!")

    except:
        print("\nAn error has occurred in Session_Info.")



if __name__ == '__main__':
    print(datetime.now())
    print("")

    user_info()
    page_info()
    platform_device_info()
    store_info()
    session_info()

    print("")
    
