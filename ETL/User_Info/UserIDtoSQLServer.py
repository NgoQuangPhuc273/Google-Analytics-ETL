import pyodbc
import pandas as pd
import numpy as np

def load():
     df = pd.read_csv("C:/Users/DELL/Desktop/Projects/Google-Analytics-ETL/files/UserId.csv")
     df = df.astype(str)


     server = 'DESKTOP-75CF3H4\SQLEXPRESS' 
     database = 'KPIM_Google_Analytics' 
     username = 'sa' 
     password = 'Neverland1' 

     cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='
                              +server
                              +';DATABASE='+database
                              +';UID='+username
                              +';PWD='+ password)

     cursor = cnxn.cursor()

     #Truncate table
     cursor.execute("TRUNCATE TABLE UserId")

     # Insert Dataframe into SQL Server:
     for index, row in df.iterrows():
          cursor.execute("INSERT INTO UserId (Client_Id,Sessions,Avg_Session_Duration,Bounce_Rate,Revenue,Transactions,Goal_Conversion_Rate) VALUES(?,?,?,?,?,?,?)",  
          row.Client_Id,
          row.Sessions,
          row.Avg_Session_Duration,
          row.Bounce_Rate,
          row.Revenue,
          row.Transactions,
          row.Goal_Conversion_Rate

          )

     cnxn.commit()
     cursor.close()

def main():
     load()

if __name__ == '__main__':
     main()