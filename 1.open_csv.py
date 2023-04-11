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
        
        if len(dat) < 1: continue              
        cur.execute('SELECT Day from stocks where Day = ?', (dat,))
        line = cur.fetchone()
        #checking if a record alredy exists
        if line is None:
            print('Inserting: Day ', dat,'Price ', val)
            cur.execute('INSERT INTO stocks(Day, Price) VALUES (?, ?)', (dat, val,))
            #print inserting data
        else:
            print('Record already exists')
        conn.commit()
  
print('Done')
conn.close()
