import json  as js
import datetime as dt
import pytz as pz
import pylab as plt

d = -1 #Definert som -1, fordi den vil starte med å si at det ikke er samme dag i dag som ved forrige tid.
prev_time = None

start_locations = {}
dates = []
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekdays = [0, 0, 0, 0, 0, 0, 0]

with open("Data eksempeleksamen/Eksempeleksamen22.json", "r", encoding="ISO-8859-1") as file:
    data_frame = js.load(file)
    
    for row in data_frame:
        #############################
        ### Startstasjon oppgave: ###
        #############################

        start_station_name = row["start_station_name"]

        if start_station_name in start_locations:
            start_locations[start_station_name] += 1
        else:
            start_locations[start_station_name] = 1


        #############################
        ##### Starttid oppgave: #####
        #############################

        date_str = row["started_at"]
        
        # Gi riktig ISO-format, siden den er i feil format.
        date_str = date_str[:-6]
        date_dt = dt.datetime.fromisoformat(date_str + "+00:00").replace(tzinfo=pz.UTC)
        
        # Konverter tidssone, hvis jeg skal ha samme tid ut som i filen, å jeg ha en 00:00 tidssone, og Dakar er en av dem.
        local_tz = pz.timezone('Africa/Dakar') 
        local_dt = date_dt.astimezone(local_tz)
        
        # Ta bare år, måned og dag, siden jeg skal bare sammenligne de.
        date = local_dt.strftime('%Y%m%d')
        dates.append(date)

        #Finne ut om det er den samme dagen som den før, hvis ikke så bytter den til neste.
        if date != prev_time:
            if d < 6:
                d += 1
            else:
                d = 0
        weekdays[d] += 1
        prev_time = date
file.close()
sorted_items = list(sorted(start_locations.items(), key=lambda item: item[1], reverse=True))
top_items = sorted_items[:3]
top_dict = {}
for key, value in top_items:
    top_dict[key] = value
print(f"De tre mest vanlige lokalisjonene er: {top_dict}")
bottom_items = sorted_items[-3:]
bottom_dict = {}
for key, value in bottom_items:
    bottom_dict[key] = value
print(f"De tre minst vanlige lokalisjonene er: {bottom_dict}")

plt.barh(day_names, weekdays)
plt.title("Number of starting times each day of the week in a month")
plt.xlabel("Day of the week")
plt.ylabel("Number of starting times those days")
plt.show()