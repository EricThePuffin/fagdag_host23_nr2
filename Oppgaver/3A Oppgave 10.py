#I denne oppgaven skal du justere utseendet til et søylediagram du har laget tidligere. Finn ut hvordan du kan 
#tilpasse søylenes farge og bredde (eller høyde hvis du har brukt barh() ), og tilpass dem på en måte du liker. 
#Du kan også justere skrifttype og linjene rundt og i diagrammet hvis du ønsker det. 
#På worldometers kan vi finne mange interessante datasett. Gå inn på denne siden om bilproduksjon  og lag et 
#stolpediagram som viser hvor mange biler som produseres av hvert av de ti landene som produserer flest biler.
import pylab as plt

land = ["Kina", "Japan", "Tyskland", "USA", "Sør-Korea", "India", "Spania", "Mexico", "Brasil", "Storbrittania"]
biler = [24420744, 7873886, 5746808, 3934357, 3859991, 3677605, 2354117, 1993168, 1778464, 1722698]

for i in range(0, len(biler)):
    biler[i] /= 1000000
plt.barh(land, biler, color = "hotpink", height = 0.9)
plt.title("Land etter antall biler produsert")
plt.xlabel("Biler i millioner")
plt.ylabel("Produksjonsland")
plt.grid(axis="x", linestyle = "--", linewidth = 0.5)
plt.show()