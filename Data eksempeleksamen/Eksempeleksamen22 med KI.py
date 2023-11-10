#Kan du skrive en kode som søker etter de tre mest normale tingene i en csv-fil?
import pandas as pd

data_frame = pd.read_csv('Data eksempeleksamen/Eksempeleksamen22.csv')

top_3 = data_frame['start_station_name'].value_counts().nlargest(3)
bottom_3 = data_frame["start_station_name"].value_counts().nsmallest(3) #La til selv basert på koden til KI over.

print(top_3)
print(bottom_3) #Samme her.