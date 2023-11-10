#Gjør om programmet i eksemplet ovenfor slik at de to grafene havner ved siden av hverandre i stedet for nedenfor 
#hverandre.
import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(0, 20, 50)

# Graf 1
yverdier = 0.5*xverdier**2 

plt.subplot(1, 2, 1)
plt.plot(xverdier, yverdier)
plt.grid()

# Graf 2
yverdier = -0.3*xverdier**3 

plt.subplot(1, 2, 2)
plt.plot(xverdier, yverdier)
plt.grid()

plt.show()