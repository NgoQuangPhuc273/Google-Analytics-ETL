# Google-Analytics-ETL

This is an demo ETL to load Users and Sessions data from Google Analytics Page of KPIM's Webstore: [ga.kpim.vn](https://ga.kpim.vn/).

I. Brief steps:

    1. Connect Google Analytics with ga.kpim.vn
    
    2. Set up credentials using console.google
    
    3. Extract data to local storage
    
    4. Transform data
    
    5. Load transformed data into SQL Server Database


II. Required libraries and tools:

    1. Python 3.10
    2. Numpy
    3. Pandas
    4. pyodbc
    5. httplib2
    6. googleapiclient
    7. oauth2client
    8. datetime
    9. sys