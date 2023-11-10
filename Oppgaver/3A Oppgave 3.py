#Tegn grafen til funksjonen f(x) = 2x – 3. 
#   Juster utseendet til grafen ved å bruke innebygde stiler. Prøv minst fem forskjellige stiler.
#   Juster utseendet til grafen uten å bruke en innebygd stil. Prøv deg fram med ulike farger og andre egenskaper.
import matplotlib.pyplot as plt
import numpy as np
import random as r

def f(x):
    return 2*x - 3

xverdier = np.linspace(-10, 10, 21) 
yverdier = f(xverdier)

styles = plt.style.available

plt.subplot(2, 3, 1)
plt.plot(xverdier, yverdier, color ="olive", linestyle="dashed", zorder=1)
plt.title("Egen")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.axhline(0, color="black", zorder=0)
plt.axvline(0, color="black", zorder=0)

for i in range(2, 7):
    style = r.choice(styles)
    plt.subplot(2, 3, i)
    plt.plot(xverdier, yverdier, zorder = 1)
    plt.style.use(style)
    plt.title(style)
    styles.remove(style)

plt.show()