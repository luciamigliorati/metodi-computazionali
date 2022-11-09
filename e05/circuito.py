from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def vin(t):
    v=0
  #int() per gli scalari(o as type per gli array) legge in quel momento t un int (altrimenti non va %)
    if(int(t)%2==0):
       return 1
    else:
       return -1

def f(vout,t,vinf,rc):#definisco la funzione a secondo membro
    return  (vinf(t)-vout)/rc#generica funzione vinf

a=0#inf intervallo tempo
b=10#sup intervallo tempo
n=10000 #numero intervalli
h=(b-a)/n#passo
v0=0#condizione iniziale sulla soluzione
rc=1#costante di tempo del circuito

tt = np.arange(a,b,h)#tempo discreto per integrare
vout = np.empty(0)

vout1=integrate.odeint(f, v0, tt, args=(vin,rc))#specificare i parametri liberi; specifo la funzione vin che deve usare -->in questo caso vinf definita all'inizio
vin_array=((tt.astype(int)+1)%2)*2-1
#for i in range(tt):
  # vin_array=vin(i)

#grafico soluzione
plt.plot(tt, vout1)
plt.xlabel('tempo')
plt.ylabel('soluzione')
#grafico Vin
plt.plot(tt, vin_array)
plt.show()

rc=0.1


vout2=integrate.odeint(f, v0, tt, args=(vin,rc))#specificare i parametri liberi; specifo la funzione vin che deve usare -->in questo caso vinf definita all'inizio


#grafico soluzione
plt.plot(tt, vout2)
plt.xlabel('tempo')
plt.ylabel('soluzione')
#grafico Vin
plt.plot(tt, vin_array)
plt.show()

rc=0.01

vout3=integrate.odeint(f, v0, tt, args=(vin,rc))#specificare i parametri liberi; specifo la funzione vin che deve usare -->in questo caso vinf definita all'inizio


#grafico soluzione
plt.plot(tt, vout3)
plt.xlabel('tempo')
plt.ylabel('soluzione')
#grafico Vin
plt.plot(tt, vin_array)
plt.show()


#####csv

#per creare una tabella e' prima necessario definire un dizionario
dict = {'tempi': tt, 'Vin': vin_array, 'Vout RC=1': vout1[:,0],'Vout RC=0,1': vout2[:,0], 'Vout RC=0,01': vout3[:,0]}
#la soluzione dell'eq diff si presenta come una sorta di matrice quindi con [:,0] estrapola la prima colonna

#tabella
df=pd.DataFrame(data=dict)
#salvataggio in csv
df.to_csv('Tabella_filtro.csv')
