import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
   
    Get sales figure input from the user
    """
    print('Please enter sales data from last maraket.')
    print('data should be six numbers, seperated by commas.')
    print('Exsample: 10,20,30,4050,60\n')

    data_str = input('Enter your data heer: ')
    print(f'The data provided is {data_str}')


get_sales_data()