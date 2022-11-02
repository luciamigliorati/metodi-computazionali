import numpy as np
import pandas as pd
from scipy import optimize
from numpy import mean
import math 
import matplotlib.pyplot as plt

'''Minimizzazione
Fit di una serie di dati
il file di dati fit_data.csv contiene dei valori per le variabili x e y;
i valori di  possono essere considerati dei conteggi e seguono la statistica poissoniana;
si può ipotizzare che i dati rappresentino una curva lognormale (gaussiana nel logaritmo dei valori di );
creare uno script python che:
legga il file di dati fit_data.csv;
produca un grafico di  in funzione di  nella forma più appropriata;
creare un secondo script python che:
definisca una funzione lognormale da usare per il fit dei dati;
legga il file di dati fit_data.csv;
esegua il fit dei dati con la funzione lognormale;
produca il grafico della funzione di fit ottimizzata sovrapposta ai dati;
stampi il valore dei parametri del fit e del chi quadrato;
SUGGERIMENTO: esplorare la possibilità di mostrare uno o entrambi gli assi dei grafici in maniera logaritmica.'''

#distribuzione poissoniana delle y significa che l'errore e la radice delle y

data=pd.read_csv('fit_data.csv')

#dati estratti dal file
x=data['x'].values#misura
y=data['y'].values#frequenze misure

print(x)

#PARTE I
errori_y=np.sqrt(y)


plt.errorbar(x,y,yerr=errori_y, color='salmon', fmt='o-')
plt.xlabel('numero misure')
plt.ylabel('misure')
plt.show()

#PARTE II

#funzione del fit

def gaussiana_lognorm(x, media, sigma, normalizzazione):
    logx=np.log(x)
    #gauss=np.zeros(len(x))
    #for i in range(len(x)):
    #    gauss[i]=(normalizzazione*math.exp(-0.5*((logx[i]-media)/sigma)**2))/x[i]
    gauss=(normalizzazione*np.exp(-0.5*((logx-media)/sigma)**2))/x
    return gauss

#fit

params, params_covariance = optimize.curve_fit(gaussiana_lognorm, x, y)
print('media fittata', params[0])
print('sigma_fittata',params[1] )
print('coefficiente normalizzazione', params[2])
print('errore su media fittata',params_covariance[0,0])
print('errore su sigma fittata',params_covariance[1,1])
print('errore su coefficiente normalizzaziione fittato',params_covariance[2,2])

#grafico del fit

xfit=np.log(x)
yfit = gaussiana_lognorm(x, params[0], params[1], params[2])

plt.plot(xfit, yfit,color='limegreen')



#grafico delle misure(x log delle misure, y densita di probabilita)
plt.errorbar(xfit,y,yerr=errori_y, color='salmon', fmt='o-')
plt.xlabel('numero misure')
plt.ylabel('misure')
plt.savefig('minimizzazione.png')
plt.savefig('minimizzazione.pdf')
plt.show()

#chi quadro
yfit = gaussiana_lognorm(x, params[0], params[1], params[2])


chi2 =  np.sum( (yfit - y)**2 /y ) 

# gradi di libertà
ndof = len(x)-len(params)

print('chi2', chi2)
print('chi2 ridotto', chi2/ndof)
