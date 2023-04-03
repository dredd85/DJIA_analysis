import csv

with open('DJIA.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        row = row[0]
        split_row = row.split(",") #now we have list with two values
        print(split_row) 
