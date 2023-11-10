#Gjennomfør en spørreundersøkelse i klassen din der du finner ut av hvordan medelevene kommer seg til og fra skolen. 
#Del opp i kategorier som «går», «sykler», «buss», «moped» og «bil», og lag både et liggende og et stående 
#stolpediagram som viser resultatene.
import pylab as plt
fartøy = ["går", "sykler", "kollektiv", "moped", "bil"]
antall = [0, 0, 0, 0, 0]

plt.barh(fartøy, antall)
plt.grid(axis = "x")
plt.show()