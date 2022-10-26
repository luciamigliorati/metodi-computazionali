import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import integrate

#accede ai dati di vel_vs_time e li stampa
data=pd.read_csv('vel_vs_time.csv')
print(data)

#grafico

plt.plot(data['t'], data['v'])#t e v sono i nomi delle colonne presenti nel file da cui ho estratto i dati
plt.xlabel('tempo')
plt.ylabel('velocita')
plt.show()

#calcolare distanza percorsa in funzione del tempo
'''y=np.zeros(len(data['v']))
for i in range(len(data['v'])):
   y[i]=data['v'][i]
               
x=np.zeros(len(data['t']))
for i in range (len(data['t'])):
     x[i]=data['t'][i]'''

y=data['v']#immagazzina tutti i valori nell'array y senza ciclo for
x=data['t']
integrale=integrate.simpson(y,x)#i parametri sono tutti opzionale tranne y, se gli fornisco le x calcola automaticamente il passo. Oppure posso dargli il passo e non le x, se non specifo ne le x ne il passo, integra con passo 1
print('integrale',integrale)# printa la x finale


yy=np.zeros(len(data['t']))

for i in range(len(data['t'])):
    integrale=integrate.simpson(y[0:i+1],x[0:i+1])#indica l'intervallo di elementi dell'array che considero
    yy[i]=integrale
    print('integrale ',0,'-', i+1,integrale)


plt.plot(x,yy, color='salmon')
plt.xlabel('tempo')
plt.ylabel('distanza')
plt.show()
               
               
            
               
 



    
    
    











