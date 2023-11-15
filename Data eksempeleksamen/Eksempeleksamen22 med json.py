import json  as js
import datetime as dt
import pytz as pz

dates = []

with open("Data eksempeleksamen/Eksempeleksamen22.json", "r", encoding="ISO-8859-1") as file:
    data_frame = js.load(file)
    
    for row in data_frame:
        date_str = row["started_at"]
        
        # Fjern bruke Z / offset +00:00
        date_str = date_str[:-6]
        date_dt = dt.datetime.fromisoformat(date_str + "+00:00").replace(tzinfo=pz.UTC)
        
        # Konverter til lokal tidsson
        local_tz = pz.timezone('Europe/Oslo')
        local_dt = date_dt.astimezone(local_tz)
        
        # Konverter datoen til ønsket format
        date = local_dt.strftime('%Y%m%d')
        dates.append(date)

        ###
print(date_dt, "     ", local_dt, "     ", date)

file.close()