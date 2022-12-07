import numpy as np


def somma_n_naturali(n):
    somma=0
    for i in range(n+1):
     somma=somma+i
    print(somma)
    return somma

def somma_n_radici(n):
    somma=0
    for i in range(n+1):
     somma=somma+np.sqrt(i)
    print(somma)
    return somma


