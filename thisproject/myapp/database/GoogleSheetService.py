from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pprint
import csv
import json
scope = ['https://www.googleapis.com/auth/spreadsheets']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1yUk7diI2FQClHv7B_5bHz8dfOO5ccsgRSIy60NpCZsc/edit?usp=sharing")
worksheet = sheet.get_worksheet(0)
results = worksheet.get_all_records()
pp = pprint.PrettyPrinter()
pp.pprint(results)

# with open('data.csv', 'w') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     csv_writer.writerow(results)
#     # csv_writer.writerow(sales)
# json = json.dumps(results)
# f = open("dict.json","w")
# f.write(json)
# f.close()
# print(f)
