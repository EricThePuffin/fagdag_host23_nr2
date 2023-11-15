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
import csv

title = []
header = []
data = []

with open("Data næringer/omsetning.csv", "r", encoding="ISO-8859-1", newline='\r\n') as file:
    reader = csv.reader(file, delimiter = ";")
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