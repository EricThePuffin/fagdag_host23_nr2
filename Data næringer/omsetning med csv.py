"""
import pandas as pd

data = []
header = []

with open() as file:
    data_frame = pd.read_csv(file)
    i = 0
    for row in data_frame:
        if not (row):
            continue
        print(row)
        if i == 0:
            header = row
        else:
            data.append(row)
            print(row)
        i = 1
print(data)
"""
"""
import csv

title = []
header = []
data = []

with open("Data næringer/omsetning.csv", "r", encoding="ISO-8859-1", newline='\r\n') as file:
    csv_reader = csv.csv_reader(file, delimiter = ";")
    i = 0
    for row in file:
        if i == 0:
            title.append(row)
        elif i == 1:
            header.append(row)
        elif not (row):
            continue
        else:
            data.append(row)
        i += 1
print(title)
print(header)
print(data)
"""
import csv


with open("Data næringer/omsetning.csv", mode='r', newline='', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file, delimiter=';', skipinitialspace=True)
    print("------------------------------")
    for row in csv_reader:
        print(row)
    
    # reset file pointer
    file.seek(0)
    
    # skip header row
    next(csv_reader)
    
    # sort data by first column
    #sorted_list = sorted(csv_reader, key=lambda row: row[1] if len(row)>=2 else "")
    print("------------------------------")
    #for row in sorted_list:
    #    print(row)