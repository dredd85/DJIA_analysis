import csv
import sqlite3

fstock = input('Choose a csv file to upload:')
if len(fstock) < 1:
    print('File not loaded')
    exit()

conn = sqlite3.connect('DJIA.sqlite')
cur = conn.cursor()

print('Connected to database')
cur.execute('CREATE TABLE IF not EXISTS stocks (Day DATE, Price INT)')

with open(fstock, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    print('Inserting data will begin shortly')
    
    for row in spamreader:
        row = row[0]        
        split_row = row.split(",") #now we have list with two values
        dat = split_row[0][1:-1]
        val = split_row[1]
