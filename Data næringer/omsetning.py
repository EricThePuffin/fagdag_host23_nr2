import pandas as pd

data = []
header = []

with open("Data næringer/omsetning.csv", "r", encoding="ISO-8859-1") as file:
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