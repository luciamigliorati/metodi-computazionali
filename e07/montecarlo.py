import sys
import numpy as np
import scipy 
import matplotlib.pyplot as plt
import math 
#diffusione 2D
def random_walk2d(step, N):
   deltax= np.zeros(N+1)
   deltay= np.zeros(N+1)
   posizionex=np.array([0])
   posizioney=np.array([0])
   spostamentox=0
   spostamentoy=0
  
   angoli=np.random.uniform(low=0.0, high=2*math.pi, size=N)
   deltax=step*np.cos(angoli)
   deltay=step*np.sin(angoli)

   for i in deltax:
       spostamentox=spostamentox+i
       posizionex=np.append(posizionex,spostamentox)
       
   for i in deltay:
       spostamentoy=spostamentoy+i
       posizioney=np.append(posizioney,spostamentoy)
   print(posizioney)
       
   return posizionex, posizioney


x1,y1=random_walk2d(1,100)
x2,y2=random_walk2d(1,100)
x3,y3=random_walk2d(1,100)
x4,y4=random_walk2d(1,100)
x5,y5=random_walk2d(1,100)

plt.plot(x1,y1, color='limegreen')
plt.plot(x2,y2, color='orchid')
plt.plot(x3,y3, color='salmon')
plt.plot(x4,y4, color='cyan')
plt.plot(x5,y5, color='magenta')
plt.show()

    


        
              


    
        
        
            


    
