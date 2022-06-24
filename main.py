import UserETL
import UsertoSQLServer

if __name__ == '__main__':

    #Get data from Google Analytics to local 
    try:
        UserETL.main()
        UsertoSQLServer.load()
        
        print("Successfully Extract, Tranform and Load!")

    except:
        print("An error has occurred.")

