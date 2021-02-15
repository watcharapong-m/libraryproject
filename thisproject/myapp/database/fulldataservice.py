# # beautisoup
# import requests

# list_url = ["601234567890.json", "README.md"]
# for i in list_url:
#     if i != "README.md":
#         url2 = requests.get("http: // projectcs.sci.ubu.ac.th/WatcharapongNasaree/libraryproject/raw/master/%22+i")
#         soup = BeautifulSoup(url2.content, "html.parser")
#         print(soup)
import sqlite3
from urllib import request
from bs4 import BeautifulSoup
import json
url = "http://projectcs.sci.ubu.ac.th/WatcharapongNasaree/libraryproject"
html = request.urlopen(url).read().decode('utf8')
html[:60]

soup = BeautifulSoup(html, 'html.parser')
list_data = []
for title in soup.find_all("a", {"class": "str-truncated"}):
    data = title.find("span")
    dataclean = data.get_text()
    if dataclean != "README.md":
        list_data.append(dataclean)
# print(list_data)


# data_true = ["Name","StudentID","ProjectName","Type","GraduationYear","GraduationYear","Abstract","Keyword","Technology","Award","LinkGit"]
base_url = "http://projectcs.sci.ubu.ac.th/WatcharapongNasaree/libraryproject/raw/master/"
success_list = []
for i in list_data:
    semi_url = base_url+i
    soup = request.urlopen(semi_url).read().decode('utf8')
    # print(soup)
    data = json.loads(soup)
    data_dict =	[
        '',
        data['Name'],
        int(data['StudentID']),
        data['ProjectName'],
        data['Type'],
        data['GraduationYear'],
        data['Abstract'],
        data['Keyword'],
        data['Technology'],
        data['Award'],
        data['LinkGit'],
    ]
    success_list.append(data_dict)

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
for i in success_list:
    cursor.execute("INSERT INTO DataTable VALUES(?,?,?,?,?,?,?,?,?,?,?)", i)
    connection.commit()
connection.close()



    # print(int(data['StudentID']))
#     success_list.append(data)
# json_formatted_str = json.dumps(success_list, indent=2)
# print(json_formatted_str)
    # print(success_list)
    # data_success
    # for i in data:
    #     data_full = data[i]
    #     print(data_full)

# print('\n{} Records Transferred'.format(no_records))
