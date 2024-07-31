# ---------------------------------------------------------------------------- #
#                                 CSV handling                                 #
# ---------------------------------------------------------------------------- #
# Ref: Automate the Boring Stuff with Python_ Practical Programming for Total Beginners 
#       chapter 8

import csv
import os

os.chdir('0011_file_handling/csv')

# --------------------------- Reading data from CSV -------------------------- #
dataList = []
timeZoneCsv = None

try:
    with open("timezone.csv") as f:
        timeZoneCsv = csv.reader(f)
        dataList = list(timeZoneCsv)
except Exception as e:
    print(e)
    
print(dataList[0:3])
print(dataList[1][1])

# ---------------------------- Writing data to CSV --------------------------- #
#! On Windows, pass a blank string for the open() function’s newline keyword argument. 
#! if you forget to set the newline argument, the rows in output.csv will be double-spaced,

with open("output.csv", "w", newline='') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(['apple', 'orange', 'banana', 'Cluster beans'])
    csvWriter.writerow([234, 342, 543, 345])
    csvWriter.writerow(['Fruit', 'Fruit', 'Fruit', 'Vegetable'])
    
# ----------------------- delimiter and lineterminator ----------------------- #
with open("output_2.csv", "w", newline='') as f:
    csvWriter = csv.writer(f, delimiter='\t', lineterminator='\n\n')
    csvWriter.writerow(['apple', 'orange', 'banana', 'Cluster beans'])
    csvWriter.writerow([234, 342, 543, 345])
    csvWriter.writerow(['Fruit', 'Fruit', 'Fruit', 'Vegetable'])