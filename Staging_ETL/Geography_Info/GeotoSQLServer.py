import pyodbc
import pandas as pd
import numpy as np

def load():
     df = pd.read_csv("files/Staging/Geography_Info.csv")
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
     cursor.execute("TRUNCATE TABLE Geography_Info")

     # Insert Dataframe into SQL Server:
     for index, row in df.iterrows():
          cursor.execute("INSERT INTO Geography_Info (ga_dateHourMinute,ga_continent,ga_country,ga_cityId,ga_city,ga_latitude,ga_longitude,ga_visits) VALUES(?,?,?,?,?,?,?,?)",  
          row.ga_dateHourMinute,
          row.ga_continent, 
          row.ga_country, 
          row.ga_cityId, 
          row.ga_city, 
          row.ga_latitude, 
          row.ga_longitude, 
          row.ga_visits, 
          )

     cnxn.commit()
     cursor.close()

def main():
     load()

if __name__ == '__main__':
     main()