#Tegn grafene til disse fire funksjonene i én felles figur:
#   y = 2*x + 1
#   y = x^2 – 3
#   y = 2**x
#   y = x/3
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x + 1

def g(x):
    return x**2 - 3

def h(x):
    return 2**x

def i(x):
    return x/3

xverdier = np.linspace(0, 10, 22)
yverdier = f(xverdier)
plt.plot(xverdier, yverdier, label = "$2*x + 1$")

yverdier = g(xverdier)
plt.plot(xverdier, yverdier, label = "$x^2 - 3$")

yverdier = h(xverdier)
plt.plot(xverdier, yverdier, label = "$2^x$")

yverdier = i(xverdier)
plt.plot(xverdier, yverdier, label = "$x/3$")
plt.grid()
plt.legend()
plt.show()