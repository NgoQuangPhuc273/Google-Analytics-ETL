import pyodbc
import pandas as pd
import numpy as np

def load():
     df = pd.read_csv("files/Staging/Platform_Device_Info.csv")
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
     cursor.execute("TRUNCATE TABLE Platform_Device_Info")

     # Insert Dataframe into SQL Server:
     for index, row in df.iterrows():
          cursor.execute("INSERT INTO Platform_Device_Info (ga_dateHourMinute,ga_browser,ga_browserVersion,ga_operatingSystem,ga_mobileDeviceBranding,ga_mobileDeviceInfo,ga_mobileDeviceModel,ga_browserSize,ga_dataSource,ga_users,ga_sessions) VALUES(?,?,?,?,?,?,?,?,?,?,?)",  
          row.ga_dateHourMinute,
          row.ga_browser, 
          row.ga_browserVersion, 
          row.ga_operatingSystem, 
          row.ga_mobileDeviceBranding, 
          row.ga_mobileDeviceInfo, 
          row.ga_mobileDeviceModel, 
          row.ga_browserSize, 
          row.ga_dataSource,
          row.ga_users,
          row.ga_sessions 
          )

     cnxn.commit()
     cursor.close()

def main():
     load()

if __name__ == '__main__':
     main()