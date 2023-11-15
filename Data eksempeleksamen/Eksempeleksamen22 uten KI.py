import pandas as pd
import pylab as plt

previous_start_day = None
startsteder = {}
d = 0
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekdays = [0, 0, 0, 0, 0, 0, 0]
with open("Data eksempeleksamen/Eksempeleksamen22.csv", "r", encoding="ISO-8859-1") as file:
    data_frame = pd.read_csv(file)
    data_frame['started_at'] = pd.to_datetime(data_frame['started_at'])
    data_frame['start_date'] = data_frame['started_at'].dt.date
    for start_station_name in data_frame["start_station_name"]:
        if start_station_name in startsteder:
            startsteder[start_station_name] += 1
        else:
            startsteder[start_station_name] = 1
    for start_date in data_frame["start_date"]:
        weekdays[d] += 1
        if start_date != previous_start_day:
            if d < 6:
                d += 1
            else:
                d = 0
        previous_start_day = start_date
print(weekdays)
mest_vanlige_startsteder = dict(sorted(startsteder.items(), key=lambda item: item[1], reverse=True))
for i, k in enumerate(mest_vanlige_startsteder.keys()):
    if i == 3:
        break
    print(k, mest_vanlige_startsteder[k])

mest_uvanlige_startsteder = dict(sorted(startsteder.items(), key=lambda item: item[1]))
for i, k in enumerate(mest_uvanlige_startsteder.keys()):
    if i == 3:
        break
    print(k, mest_uvanlige_startsteder[k])
file.close()

plt.barh(day_names, weekdays)
plt.title("Number of starting times each day of the week in a month")
plt.xlabel("Day of the week")
plt.ylabel("Number of starting times those days")
plt.show()