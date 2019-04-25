import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import pprint



scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/juan/Desktop/Time/Python/Python access-fdc7d72e2563.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('Python Test').sheet1




#password_file = open('/Users/juan/Desktop/Time/Python/password.txt')
#check = password_file.read()
#print(check)
user_input = raw_input('Include your User Name: ' )
password_input = raw_input('include your password: ')

user_names = wks.col_values(1)
user_list = []

password_numbers = wks.col_values(2)
password_list = []

for password in password_numbers:
    password_list.append(password)

for item in user_names:
    user_list.append(item)

if user_input in user_list and password_input in password_list:
    print('password and user name matches')
    if password_input == '12345':
        print('That is an easy password. Please change it')

else:
    print('That password do not match any records')
