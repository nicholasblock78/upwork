from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pandas as pd

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '13oCiOk0o8GqU9zRvfEFs9r6-QaUuFTvAmANt4pLZAac'
    RANGE_NAME = 'Live Sites to Review!A2:M6'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    #PANDAS

    df = pd.DataFrame(values)

    #rename column Headers
    #https://chrisalbon.com/python/data_wrangling/pandas_rename_column_headers/
    headers = df.iloc[0]
    print(headers)
    df = df[1:]
    df.columns = headers

    # #Pandas To Excel
    # writer = pd.ExcelWriter('output.xlsx')
    # df.to_excel(writer,'Sheet1')
    # writer.save()

    df.to_csv('test_csv.csv')

    # if not values:
    #     print('No data found.')
    # else:
    #     print('Client Name, PDP Link Used:')
    #     for row in values:
    #         # Print columns A and E, which correspond to indices 0 and 4.
    #         print('end')
    #         print('%s, %s' % (row[0], row[12]))



if __name__ == '__main__':
    main()
