import pandas as pd
from datetime import datetime
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import numpy as np

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'json/client_secrets.json'
VIEW_ID = '269455217'


def initialize_analyticsreporting():
    # Create service credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        KEY_FILE_LOCATION, SCOPES)

    # Create a service object
    http = credentials.authorize(httplib2.Http())

    analytics = build('analyticsreporting', 'v4', http=http, discoveryServiceUrl=(
        'https://analyticsreporting.googleapis.com/$discovery/rest'))

    return analytics

# Get one report page

def get_report(analytics, pageTokenVar):
    return analytics.reports().batchGet(
        body={

            'reportRequests': [
                {
                    'viewId': VIEW_ID,
                    'dateRanges': [{'startDate': '100daysAgo', 'endDate': 'today'}],
                    'metrics': [
                        {'expression': 'ga:pageviews'},
                        {'expression': 'ga:timeOnPage'},
                        {'expression': 'ga:pageviewsPerSession'},
                        {'expression': 'ga:avgTimeOnPage'}

                    ],

                    'dimensions': [
                        {'name': 'ga:dateHourMinute'},
                        {'name': 'ga:city'},
                        {'name': 'ga:country'},
                        {'name': 'ga:deviceCategory'},
                        {'name': 'ga:pagePath'},
                        {'name': 'ga:exitPagePath'},
                        {'name': 'ga:pageDepth'}    
                    ],

                    'samplingLevel': 'LARGE',
                    'pageSize': 10000
                }]
        }

    ).execute()

# Extracting Data


def handle_report(analytics, pagetoken, rows):
    response = get_report(analytics, pagetoken)

    # Header, Dimentions Headers, Metric Headers
    columnHeader = response.get("reports")[0].get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get(
        'metricHeader', {}).get('metricHeaderEntries', [])

    # Pagination
    pagetoken = response.get("reports")[0].get('nextPageToken', None)

    # Rows
    rowsNew = response.get("reports")[0].get('data', {}).get('rows', [])
    rows = rows + rowsNew

    # Recursivly query next page
    if pagetoken != None:
        return handle_report(analytics, pagetoken, rows)
    else:
        # nicer results  
        nicerows = []
        
        for row in rows:
            dic = {}
            dimensions = row.get('dimensions', [])
            dateRangeValues = row.get('metrics', [])

            for header, dimension in zip(dimensionHeaders, dimensions):
                dic[header] = dimension
            
            for i, values in enumerate(dateRangeValues):
                for metric, value in zip(metricHeaders, values.get('values')):
                    if ',' in value or ',' in value:
                        dic[metric.get('name')] = float(value)
                    else:
                        dic[metric.get('name')] = float(value)

                    #Fixing title from ga: to ga_
                    new_dic = { k.replace(':', '_'): v for k, v in dic.items() }
                    
                    #Reformat datetime
                    #Access datetime column's values
                    time = list(new_dic.values())[0]

                    #Construct new time format
                    time = time[2:4] + "/" + time[4:6] + "/" + time[6:8] + " " + time[8:10] + ":" +"10"

                    date_time_obj = datetime.strptime(time, '%y/%m/%d %H:%M')

                    #Access datetime column's keys
                    fixed_time = list(new_dic.keys())[0]

                    #Save fixed datetime into new_dic in year-month-day hour-minute format
                    new_dic[fixed_time] = str(date_time_obj.strftime("%Y-%m-%d %H:%M"))
            
            nicerows.append(new_dic)

        return nicerows

def main():
    analytics = initialize_analyticsreporting()

    global dfanalytics
    dfanalytics = []

    rows = []
    rows = handle_report(analytics, '0', rows)

    dfanalytics = pd.DataFrame(list(rows))
    dfanalytics.to_csv("files/Page_General_Info.csv")


if __name__ == '__main__':
    main()
