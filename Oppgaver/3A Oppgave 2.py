#I denne oppgaven skal du tegne grafen til funksjonen f(x) = 4x3 – x5 for x-verdier mellom –2 og 2 på minst to 
#forskjellige måter. Du skal både bruke lister som du fyller, og linspace() for å lage x-verdiene. Du skal variere 
#antall x-verdier og tegne grafen flere ganger. Tegn grafene både med punkter og linjer. Bruk disse antallene:
# 5
# 10
# 20
# 50
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 4*x**3 - x**5

xverdier = np.linspace(-2, 2, 5)
yverdier = f(xverdier)

plt.subplot(2, 2, 1)
plt.plot(xverdier, yverdier)
plt.title("Med 5 punkter")


xverdier = np.linspace(-2, 2, 10)
yverdier = f(xverdier)

plt.subplot(2, 2, 2)
plt.plot(xverdier, yverdier)
plt.title("Med 10 punkter")


xverdier = np.linspace(-2, 2, 20)
yverdier = f(xverdier)

plt.subplot(2, 2, 3)
plt.plot(xverdier, yverdier)
plt.title("Med 20 punkter")


xverdier = np.linspace(-2, 2, 50)
yverdier = f(xverdier)

plt.subplot(2, 2, 4)
plt.plot(xverdier, yverdier)
plt.title("Med 50 punkter")


plt.show()