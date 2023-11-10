#Tegn grafer som viser de fem første gangetabellene i samme figur. Det betyr at du skal tegne grafene til 
#funksjonene y = x, y = 2x, y = 3x, …, y = 5x. Langs x-aksen skal du ha tallene 1–10.
import pylab as plt
import numpy as np

def y(x, n):
    return n*x

xverdier = np.linspace(1, 10, 10)
for i in range (1, 6):
    yverdier =[]
    for n in range (1, 11):
        yverdier.append(y(i, n))
    plt.plot(xverdier, yverdier, zorder=1)
    plt.scatter(xverdier, yverdier, marker= "o", s= 5, zorder=2)
plt.axhline(1, color="black", label="1", zorder=0)
plt.axvline(1, color="black", label="1", zorder=0)
plt.legend()
plt.grid()
plt.show()