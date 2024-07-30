# ---------------------------------------------------------------------------- #
#                                 CSV handling                                 #
# ---------------------------------------------------------------------------- #

import csv
import os

os.chdir('0011_file_handling/csv')

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


