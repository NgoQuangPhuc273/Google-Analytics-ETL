import sys

sys.path.insert(0, 'Staging_ETL/User_Info')
sys.path.insert(0, 'Staging_ETL/Page_Info')
sys.path.insert(0, 'Staging_ETL/Store_Info')
sys.path.insert(0, 'Staging_ETL/Session_Info')
sys.path.insert(0, 'Staging_ETL/Platform_Device_Info')
sys.path.insert(0, 'Staging_ETL/Geography_Info')

from datetime import datetime

import User_General_ETL
import User_General_toSQLServer
import User_Detailed_ETL
import User_Detailed_toSQLServer
import UserIDtoSQLServer

import GeoETL
import GeotoSQLServer

import Page_General_ETL
import Page_General_toSQLServer
import Page_Detailed_ETL
import Page_Detailed_toSQLServer

import PlatformDeviceETL
import PlatformDevicetoSQLServer

import ProductETL
import ProducttoSQLServer

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
        Page_General_ETL.main()
        Page_General_toSQLServer.load()

        print("\nSuccessfully Extract, Tranform and Load Page_General_Info!")

    except:
        print("\nAn error has occurred in Page_General_Info.")
    
    try:
        Page_Detailed_ETL.main()
        Page_Detailed_toSQLServer.load()

        print("Successfully Extract, Tranform and Load Page_Detailed_Info!")

    except:
        print("\nAn error has occurred in Page_Detailed_Info.")


def platform_device_info():
    try:
        PlatformDeviceETL.main()
        PlatformDevicetoSQLServer.load()

        print("\nSuccessfully Extract, Tranform and Load Platform_Device_info!")

    except:
        print("\nAn error has occurred in Platform_Device_info.")


def product_info():
    #Get Page data from Google Analytics to local 
    try:
        ProductETL.main()
        ProducttoSQLServer.load()

        print("\nSuccessfully Extract, Tranform and Load Product_info!")

    except:
        print("\nAn error has occurred in Product_info.")

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
    product_info()
    session_info()

    print("")
    
