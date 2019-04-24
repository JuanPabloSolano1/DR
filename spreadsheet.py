import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import pprint



scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/juan/Desktop/Time/Python/Python access-fdc7d72e2563.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('Python Test').sheet1
glist = wks.get_all_values()

pp = pprint.PrettyPrinter()

pp.pprint(glist)

result = wks.col_values(2)
pp.pprint(result)

result1 = wks.row_values(3,0)
pp.pprint(result1)

result2 = wks.cell(3,3).value
pp.pprint(result2)

wks.update_cell(3,3,'35%')

result3 = wks.update_cell(4,2,'1,267')
pp.pprint(result3)


result5 = wks.findall('Palo Alto')
pp.pprint(result5)

cell_list = wks.range('A1:C7')

for cell in cell_list:
    cell.value = 'Scrutis ok '

# Update in batch
wks.update_cells(cell_list)

row = ['i', 'am', 'updating']
index = 2

wks.insert_row(row,index)

row1 = ['SCRUTISSSSSSSSSS','I', 'Want ', 'to','watch', 'a', 'show', 'NOWWWWWWWWWW']
index2 = 3

result8 = wks.insert_row(row1,index2)
pp.pprint(result8)

wks.update_acell('A2','hello there')

result4 = wks.acell('A1').value
pp.pprint(result4)
