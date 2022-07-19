import pyodbc
import pandas as pd
import numpy as np

def load():
     df = pd.read_csv("files/Staging/Product_Info.csv")
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
     cursor.execute("TRUNCATE TABLE Product_Info")

     # Insert Dataframe into SQL Server:
     for index, row in df.iterrows():
          cursor.execute("INSERT INTO Product_Info (ga_productName,ga_transactionId,ga_itemQuantity,ga_itemRevenue,ga_uniquePurchases,ga_revenuePerItem,ga_itemsPerPurchase,ga_productRefundAmount,ga_buyToDetailRate,ga_cartToDetailRate) VALUES(?,?,?,?,?,?,?,?,?,?)",  
          row.ga_productName,
          row.ga_transactionId,
          row.ga_itemQuantity,
          row.ga_itemRevenue,
          row.ga_uniquePurchases,
          row.ga_revenuePerItem,
          row.ga_itemsPerPurchase,
          row.ga_productRefundAmount,
          row.ga_buyToDetailRate,
          row.ga_cartToDetailRate
          )

     cnxn.commit()
     cursor.close()

def main():
     load()

if __name__ == '__main__':
     main()