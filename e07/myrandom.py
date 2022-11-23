import sys
import numpy as np
import matplotlib.pyplot as plt
import math

def invcum(y):
    x=2*np.arccos(1-2*y)
    return x


nsample=10000
yrndq = np.random.random(nsample)

# valori x da cumulativa inversa
xrndq = invcum(yrndq)

fig, ax = plt.subplots(1,2, figsize=(11,5))
ax[0].hist(yrndq, bins=100, range=(0,1), color='cyan',   ec='darkcyan')
ax[0].set_title('Distribuzione y Cumulativa')
ax[0].set_xlabel('y cumulativa')

ax[1].hist(xrndq, bins=100, range=(0,2*math.pi), color='orange', ec='darkorange')
ax[1].set_title('Distribuzione')
ax[1].set_xlabel('x')
plt.show()

