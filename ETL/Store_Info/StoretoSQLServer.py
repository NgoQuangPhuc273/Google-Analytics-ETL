import pyodbc
import pandas as pd
import numpy as np

def load():
     df = pd.read_csv("files/Store_Info.csv")
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
     cursor.execute("TRUNCATE TABLE Store_Info")

     # Insert Dataframe into SQL Server:
     for index, row in df.iterrows():
          cursor.execute("INSERT INTO Store_Info (ga_dateHourMinute, ga_city, ga_country, ga_deviceCategory, ga_transactionId, ga_productName, ga_productCategory, ga_itemQuantity, ga_revenuePerItem, ga_itemsPerPurchase, ga_productAddsToCart, ga_productRemovesFromCart) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",  
          row.ga_dateHourMinute,
          row.ga_city, 
          row.ga_country, 
          row.ga_deviceCategory, 
          row.ga_transactionId, 
          row.ga_productName, 
          row.ga_productCategory, 
          row.ga_itemQuantity, 
          row.ga_revenuePerItem, 
          row.ga_itemsPerPurchase,
          row.ga_productAddsToCart,
          row.ga_productRemovesFromCart
          )

     cnxn.commit()
     cursor.close()

def main():
     load()

if __name__ == '__main__':
     main()