import numpy as np
import sys,os


#definisco la classe hit
class Hit():
    
 def __init__(self,modulo,sensore,time):
        self.modulo = modulo
        self.sensore = sensore 
        self.time = time
 def __lt__(self, other):
        return self.time < other.time
 def __sub__(self,other):
     return self.time - other.time
       
class Event(): #il costruttore me lo crea vuoto
 def __init__(self):
        self.nhit = 0
        self.tfirst = 0
        self.tfirst = -1
        self.durata=-1
        self.hits=np.empty([])

#metodo che aggiorna l'oggetto event

def aggiorna_event(h):
    self.nhit=self.nhit+1
    self.hits=np.append(self.hits,h)
    self.tfirst=self.hits[0].time
    self.tlast=h.time
    self.durata=h.time-self.hits[0]

def stampa():
    print('Numero di hit totali /n', self.nhit)
    print('Time Stamp primo Hit /n', self.tfirst)
    print('Time Stamp ultimo Hit /n', self.tlast)
    print('Durata temporale /n', self.durata)
    print('Array di tutti gli Hit /n', self.hits)
    

    
    

    
    
    
