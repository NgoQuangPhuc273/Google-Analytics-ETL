import sys

sys.path.insert(0, 'ETL/User_Info')
sys.path.insert(0, 'ETL/Page_Info')

import UserETL
import UsertoSQLServer
import PageETL
import PagetoSQLServer


def user_info():
    #Get User data from Google Analytics to local 
    try:
        UserETL.main()
        UsertoSQLServer.load()

        print("Successfully Extract, Tranform and Load User_Info!")

    except:
        print("An error has occurred in User_Info.")

def page_info():
    #Get Page data from Google Analytics to local 
    try:
        PageETL.main()
        PagetoSQLServer.load()

        print("Successfully Extract, Tranform and Load Page_Info!")

    except:
        print("An error has occurred in Page_Info.")

if __name__ == '__main__':
    user_info()
    page_info()

    
