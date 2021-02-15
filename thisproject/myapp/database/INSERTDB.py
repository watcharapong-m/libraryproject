import sqlite3
import csv

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
with open('datatest.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO DataTable VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
        connection.commit()
        no_records += 1
connection.close()
print('\n{} Records Transferred'.format(no_records))

