import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope=[
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    ]

json_file_name='diesel-monitor-283800-7f744adca4c3.json'

credentials=ServiceAccountCredentials.from_json_keyfile_name(json_file_name,scope)
gc=gspread.authorize(credentials)
worksheet=gc.open("bob").worksheet("Sheet1")
#worksheet.update('A1',100)
#worksheet.update('B1',100)
