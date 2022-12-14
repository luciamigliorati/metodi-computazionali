import reco as rc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#PASSO 3

#leggo i file
data1=pd.read_csv('hit_times_M0.csv')
data2=pd.read_csv('hit_times_M1.csv')
data3=pd.read_csv('hit_times_M2.csv')
data4=pd.read_csv('hit_times_M3.csv')

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

hitarray1=np.empty(0)
hitarray2=np.empty(0)
hitarray3=np.empty(0)
hitarray4=np.empty(0)

#per ogni file creo un array di hit

for i in range(len(modulo1)):
      hitarray1 = np.append(hitarray1, np.array([ rc.Hit(modulo1[i],sensore1[i],tempo1[i]) ]) )#l'uscita rappresenta un data frame devo trasformarlo in array
for i in range(len(modulo2)):
      hitarray2 = np.append(hitarray2, np.array([ rc.Hit(modulo2[i],sensore2[i],tempo2[i]) ]))
for i in range(len(modulo3)):
      hitarray3 = np.append(hitarray3, np.array([ rc.Hit(modulo3[i],sensore3[i],tempo3[i]) ]))
for i in range(len(modulo4)):
      hitarray4 = np.append(hitarray4, np.array([ rc.Hit(modulo4[i],sensore4[i],tempo4[i]) ]))

#ordino temporalmente gli hits

hitordinati=np.empty(0)
hitordinati=np.concatenate((hitarray1, hitarray2, hitarray3, hitarray4))
hitordinati=np.sort(hitordinati)

#calcolo differenza tempi tra un hit e il successivo
deltat=np.diff(hitordinati)

#applico maschera--> differenze di tempi solo positive
mask=deltat > 0
difftime=np.zeros(len(deltat[mask]))

for i in range(len(difftime)):
    difftime[i]=np.log10(deltat[mask][i])

#faccio un istogramma
plt.hist(difftime, bins=30, color='violet')
plt.title('delta t fra hit consecutivi')
plt.show()


#in sublot per mettere scala log ax.set 










