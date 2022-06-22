import pyodbc
import pandas as pd
import numpy as np

df = pd.read_csv("users.csv")
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

# Insert Dataframe into SQL Server:
for index, row in df.iterrows():
     cursor.execute("INSERT INTO UserTable (Users, Session) values(?,?)",  
     row.Users,
     row.Session)

cnxn.commit()
cursor.close()