import pyodbc
import pandas as pd
import numpy as np


def load():
    df = pd.read_csv(
        "C:/Users/DELL/Desktop/Projects/Google-Analytics-ETL/files/User_Detailed_Info.csv")
    df = df.astype(str)

    server = 'DESKTOP-75CF3H4\SQLEXPRESS'
    database = 'KPIM_Google_Analytics'
    username = 'sa'
    password = 'Neverland1'

    cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='
                          + server
                          + ';DATABASE='+database
                          + ';UID='+username
                          + ';PWD=' + password)

    cursor = cnxn.cursor()

    # Truncate table
    cursor.execute("TRUNCATE TABLE User_Detailed_Info")

    # Insert Dataframe into SQL Server:
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO User_Detailed_Info (ga_dateHourMinute, ga_city, ga_country, ga_deviceCategory, ga_userType, ga_sessionCount, ga_daysSinceLastSession, ga_users, ga_newUsers, ga_sessionsPerUser) VALUES(?,?,?,?,?,?,?,?,?,?)",
                       row.ga_dateHourMinute,
                       row.ga_city,
                       row.ga_country,
                       row.ga_deviceCategory,
                       row.ga_userType,
                       row.ga_sessionCount,
                       row.ga_daysSinceLastSession,
                       row.ga_users,
                       row.ga_newUsers,
                       row.ga_sessionsPerUser
                       )

    cnxn.commit()
    cursor.close()


def main():
    load()


if __name__ == '__main__':
    main()
