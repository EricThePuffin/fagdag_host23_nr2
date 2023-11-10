#Tabellen nedenfor viser antall stortingsrepresentanter for Arbeiderpartiet og Høyre ved de ti siste 
#stortingsvalgene. Lag et gruppert stolpediagram som viser denne fordelingen.
import pylab as plt
import numpy as np
årstall = [1985, 1989, 1993, 1997, 2001, 2005, 2009, 2013, 2017, 2021]
arbeiderpartiet	= [71, 63, 67, 65, 43, 61, 64, 55, 49, 48]
høyre = [50, 37, 28, 23, 38, 38, 41, 48, 45, 36]

fig, ax = plt.subplots(figsize=(10, 5))

x = np.arange(10)

ax.bar(x+0.2, arbeiderpartiet, label = "Arbeiderpartiet", width = 0.5, color = "red")
ax.bar(x-0.2, høyre, label = "Høyre", width = 0.5, color = "blue")
ax.set_xticks(x, årstall)
ax.legend()

fig.subplots_adjust(left = 0.4)

ax.grid(axis = "y")
plt.title("Størrelse på AP og Høyre over de siste 10 stortingsvalgene")
plt.show()