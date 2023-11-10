import pandas as pd

startsteder = {}
with open("Data eksempeleksamen/Eksempeleksamen22.csv", "r", encoding="ISO-8859-1") as file:
    data_frame = pd.read_csv(file)
    for start_station_name in data_frame['start_station_name']:
        if start_station_name in startsteder:
            startsteder[start_station_name] += 1
        else:
            startsteder[start_station_name] = 1

mest_vanlige_startsteder = dict(sorted(startsteder.items(), key=lambda item: item[1], reverse=True))
for i, k in enumerate(mest_vanlige_startsteder.keys()):
    if i == 3:
        break
    print(k, mest_vanlige_startsteder[k])

mest_uvanlige_startsteder = dict(sorted(startsteder.items(), key=lambda item: item[1]))
for i, k in enumerate(mest_vanlige_startsteder.keys()):
    if i == 3:
        break
    print(k, mest_uvanlige_startsteder[k])
file.close()