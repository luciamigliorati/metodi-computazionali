import numpy as np
import pandas as pd
gg=np.arange(1,31,1)
temp_med= np.random.normal(loc=30, scale=10, size=30)#genera numeri casuali secondo la distribuzione normale della forma loc=valore vero, scale=sigma, size=dimensioni
temp_med.astype(int)
temp_med_err=np.ones(30)#tutti 1 per 30 volte
temp_med_err=temp_med_err*0.10
#temp=np.array([[temp_med],[temp_med_err]]
mm_pioggia=np.random.normal(loc=1, scale=0.5, size=30)
#mm_pioggia.round(1)arrotondo a una cifra decimale
mm_pioggia_err=np.random.normal(loc=0.5, scale=0.2, size=30)
#round(mm_pioggia_err,1)
mydf=pd.DataFrame(columns=['giorno', 't[°C]', 'err t', 'mm pioggia', 'err pioggia'])#nomi delle colonne in cui organizzo i dati
mydf['giorno']=gg #per associare alle colonne gli array
mydf['t[°C]']= temp_med
mydf['err t']=temp_med_err
mydf['mm pioggia']=mm_pioggia
mydf['err pioggia']=mm_pioggia_err
print(mydf)
mydf.to_csv('mydf.csv', index=False)              
              
