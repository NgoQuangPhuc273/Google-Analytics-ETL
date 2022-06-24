from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import httplib2
import pandas as pd
import numpy as np

#Create service credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('json/client_secrets.json', ['https://www.googleapis.com/auth/analytics.readonly'])

#Create a service object
http = credentials.authorize(httplib2.Http())
service = build('analytics', 'v4', http=http, discoveryServiceUrl=('https://analyticsreporting.googleapis.com/$discovery/rest'))
response = service.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': '269455217',
                'dateRanges': [{'startDate': '30daysAgo', 'endDate': 'today'}],
                'metrics': [
                    {'expression': 'ga:users'},
                    # {'expression': 'ga:pageViews'},
                    # {'expression': 'ga:bounces'},
                    # {'expression': 'ga:timeOnPage'}
                ], 
                'dimensions': [
                    # {'name': 'ga:date'},
                    # {'name': 'ga:dateHour'},
                    {'name': 'ga:dateHourMinute'},
                    # {'name': 'ga:country'},
                    # {'name': 'ga:city'},
                    # {'name': 'ga:deviceCategory'},
                ], 
                'orderBys': [{'fieldName': 'ga:users', 'sortOrder': 'DESCENDING'}], 
                'pageSize': 1000
            }]
    }
).execute()

#Create two empty lists that will hold our dimentions and users data
dim = []
val = []

#Extract Data
for report in response.get('reports', []):
  
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    rows = report.get('data', {}).get('rows', [])
  
    for row in rows:
  
        dimensions = row.get('dimensions', [])
        dateRangeValues = row.get('metrics', [])
  
        for header, dimension in zip(dimensionHeaders, dimensions):
            dim.append(dimension)
  
        for i, values in enumerate(dateRangeValues):
            for metricHeader, value in zip(metricHeaders, values.get('values')):
                val.append(value)

#Sort Data

val.reverse()
dim.reverse()

# print(val)
# print(dim)

df = pd.DataFrame() 
df["Session"] = dim
df["Users"] = val
df = df[["Users","Session"]]
df

# print(df)
#Export to CSV
df.to_csv("usersFirst.csv")

# my_list = df.columns.values.tolist()
# print(my_list)

