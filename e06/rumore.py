import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import constants, fft
from scipy import optimize

data1=pd.read_csv('/home/lm010022/metodi-computazionali/get-mcf-data/get_data.py/data_sample1.csv')

print(data1)

data2=pd.read_csv('/home/lm010022/metodi-computazionali/get-mcf-data/get_data.py/data_sample2.csv')

print(data2)

data3=pd.read_csv('/home/lm010022/metodi-computazionali/get-mcf-data/get_data.py/data_sample3.csv')

print(data3)

plt.plot(data1['time'].values, data1['meas'].values, color='springgreen', label=1)
plt.title('Data sample 1')

plt.plot(data2['time'].values, data2['meas'].values, color='salmon',label=2)
plt.title('Data sample 2')


plt.plot(data3['time'].values, data3['meas'].values, color='violet',label= 3)
plt.title('Data sample')

plt.xlabel('tempi')
plt.ylabel('rumori')
plt.show()

trasdata1=fft.fft(data1['meas'].values)
trasdata2=fft.fft(data2['meas'].values)
trasdata3=fft.fft(data3['meas'].values)

#grafico spettro di potenza

plt.plot(np.absolute(trasdata1[:trasdata1.size//2])**2, 'o', color='springgreen')
plt.plot(np.absolute(trasdata2[:trasdata2.size//2])**2, 'o', color='salmon')
plt.plot(np.absolute(trasdata3[:trasdata3.size//2])**2, 'o', color='violet')
plt.title('spettro di potenza')
plt.xlabel('Indice')
plt.ylabel(r'$|c_k|^2$')
plt.xscale('log')
plt.yscale('log')
plt.show()
#######frequenze
passo=1
snyquist = 0.5
freq1 = snyquist*fft.fftfreq(trasdata1.size, passo)
print(freq1)
freq2 = snyquist*fft.fftfreq(trasdata2.size, passo)
#print(sunf1)
freq3 = snyquist*fft.fftfreq(trasdata3.size, passo)
#print(sunf1)


#######fit della dipendenza dello spettro di potenza dalla frequenza

#funzione del fit
def noise(freq, a, beta,c):
    res=a*(1/freq**beta)+c
    return res
#fit
params, params_covariance = optimize.curve_fit(noise,freq1[1:freq1.size//2],np.absolute(trasdata1[1:trasdata1.size//2])**2)
print('costante di normalizzazione', params[0])
print('beta',params[1])
print('c', params[2])


#grafico

xfit=freq1[1:freq1.size//2]
yfit =noise(freq1[1:freq1.size//2], params[0], params[1], params[2])

plt.plot(freq1[1:freq1.size//2], np.absolute(trasdata1[1:trasdata1.size//2])**2,'o', color='springgreen')
plt.plot(xfit, yfit,'-', color='green')
plt.xlabel('Frequenze')
plt.ylabel('Potenza')
plt.title('noise 1')
plt.show()

xfit=freq2[1:freq2.size//2]
yfit =noise(freq2[1:freq2.size//2], params[0], params[1], params[2])

plt.plot(freq2[1:freq2.size//2], np.absolute(trasdata2[1:trasdata2.size//2])**2,'o', color='springgreen')
plt.plot(xfit, yfit,'-', color='green')
plt.xlabel('Frequenze')
plt.ylabel('Potenza')
plt.title('noise 2')
plt.show()

xfit=freq3[1:freq3.size//2]
yfit =noise(freq3[1:freq3.size//2], params[0], params[1], params[2])

plt.plot(freq3[1:freq3.size//2], np.absolute(trasdata3[1:trasdata3.size//2])**2,'o', color='springgreen')
plt.plot(xfit, yfit,'-', color='green')
plt.xlabel('Frequenze')
plt.ylabel('Potenza')
plt.title('noise 3')
plt.xscale('log')
plt.yscale('log')
plt.show()












