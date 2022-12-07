import somme as s #importo il modulo che ho definito
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#leggo i file
data1=pd.read_csv('hit_times_M0.csv')
data2=pd.read_csv('hit_times_M1.csv')
data3=pd.read_csv('hit_times_M2.csv')
data4=pd.read_csv('hit_times_M3.csv')

#stampo il contenuto
print(data1)
print(data2)
print(data3)
print(data4)

'''
moduli=identificatore del moduko [0-3];
sensori=identificatore del sensore [0-4];
tempi=distanza temporale in ns dall'inizio della presa dati.'''

#rinomino le colonne
modulo1=data1['mod_id']
sensore1=data1['det_id']
tempo1=data1['hit_time']

modulo2=data2['mod_id']
sensore2=data2['det_id']
tempo2=data2['hit_time']

modulo3=data3['mod_id']
sensore3=data3['det_id']
tempo3=data3['hit_time']

modulo4=data4['mod_id']
sensore4=data4['det_id']
tempo4=data4['hit_time']

#istogramma del primo esperimento--> mostra quanti e
#venti cadono in ogni intervallo la cui ampiezza dipende dai bins

plt.hist(tempo1, bins=100, color='purple')
plt.title('Hit per intervallo')
plt.show()

#creo una maschera per escludere il valore 0 di cui il log non e' definito--> la applico a delta tempi

deltatempo1=np.diff(tempo1)

mask1=deltatempo1>0
log_deltatempo1=np.log(deltatempo1[mask1])
plt.hist(log_deltatempo1, bins=100, color='cyan')
plt.title('Differenze tempi tra hit consecutivi')
plt.show()





