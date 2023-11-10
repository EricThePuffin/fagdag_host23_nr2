#Utvid det siste eksemplet ovenfor slik at du lager flere x-verdier. I eksemplet laget vi 10 x-verdier, men du ser 
#kanskje at grafen ikke blir helt glatt? Omtrent hvor mange verdier trenger vi for at grafen skal bli glatt?
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

xverdier = np.linspace(0, 10, 22) # Hva som regnes som glatt kan variere fra person til person, for meg virker 22 ganske glatt.
yverdier = f(xverdier)

plt.plot(xverdier, yverdier)
plt.show()