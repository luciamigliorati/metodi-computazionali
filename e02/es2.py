import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mydf2=pd.read_csv('mydf.csv')#legge il file es1
#grafico 1 senza errori
plt.plot(mydf2['giorno'],mydf2['t[°C]'])

plt.xlabel('giorni')
plt.ylabel('mm pioggia')
plt.show()
#grafico 2 con errori


plt.errorbar(mydf2['giorno'], mydf2['t[°C]'],yerr= mydf2['err pioggia'], fmt='o-')#fa punto e linea
plt.xlabel('giorni')
plt.ylabel('mm pioggia')
plt.show()
