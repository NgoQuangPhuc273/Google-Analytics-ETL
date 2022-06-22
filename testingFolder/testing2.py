import pyodbc
import pandas as pd

df = pd.read_csv("users.csv")

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
     cursor.execute("INSERT INTO USERS (PAGES, USERS, SESSION) values(?,?,?)", 
     row.PAGES, 
     row.USERS,
     row.SESSION)

cnxn.commit()
cursor.close()