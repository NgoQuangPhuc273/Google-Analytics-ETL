import pyodbc
import pandas as pd
import numpy as np

def load():
     df = pd.read_csv("files/Staging/Page_Detailed_Info.csv")
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
     cursor.execute("TRUNCATE TABLE Page_Detailed_Info")

     # Insert Dataframe into SQL Server:
     for index, row in df.iterrows():
          cursor.execute("INSERT INTO Page_Detailed_Info (ga_hostname,ga_pagePath,ga_pageTitle,ga_landingPagePath,ga_secondPagePath,ga_exitPagePath,ga_pageDepth,ga_pageValue,ga_entrances,ga_entranceRate,ga_pageviews,ga_uniquePageviews,ga_exits,ga_exitRate) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",  
          row.ga_hostname,
          row.ga_pagePath,
          row.ga_pageTitle,
          row.ga_landingPagePath,
          row.ga_secondPagePath,
          row.ga_exitPagePath,
          row.ga_pageDepth,
          row.ga_pageValue,
          row.ga_entrances,
          row.ga_entranceRate,
          row.ga_pageviews,
          row.ga_uniquePageviews,
          row.ga_exits,
          row.ga_exitRate
          )

     cnxn.commit()
     cursor.close()

def main():
     load()

if __name__ == '__main__':
     main()