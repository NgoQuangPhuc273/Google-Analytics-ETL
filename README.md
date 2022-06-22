# Google-Analytics-ETL

This is an demo ETL to load Users and Sessions data from Google Analytics Page of KPIM's Webstore: [ga.kpim.vn](https://ga.kpim.vn/).

Brief steps:
1. Connect Google Analytics with ga.kpim.vn
2. Set up credentials using console.google
3. Extract data to local storage
4. Transform data
5. Load transformed data into SQL Server Database


Required libraries and tools:

Python 3.10
Numpy
Pandas
pyodbc
httplib2
googleapiclient
oauth2client