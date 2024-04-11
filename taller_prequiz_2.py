#taller pre quiz 2
import numpy as np 
import matplotlib as plt
import pandas as pd 
from csv import reader as reader_csv;

import scipy.signal as signal;
import scipy.io as sio;

#1: matriz aleatoria
mtz=np.random.randint(1000, size=(200, 200, 30,1))
#print(mtz.size)

#2:quitar una dimension=dim 3
a=np.copy(mtz)
b=a.reshape(200,200,30)
#print(b.ndim)

#3: mostrar atributos de la matriz 3D(tamaño,forma,dimension)
print(b.size)
print(b.ndim)
print(b.shape)
print(b.dtype)

#4:pasar matriz a 2D
m2=b.reshape(4000,300)
print(m2.size) #se cambia la forma, pero se conserva el tamaño

#5: pasar datos de matriz a dataframe
def pasar_df(m2):

    df=pd.DataFrame(m2)
    return (df)

#6: funciones para cargar archivos .mat y .csv
def cargar(a):
    if a.endswith(".mat"):
        arch_cargar=scipy.io.loadmat(a)
        return (arch_cargar)

    else:
        a.endswith(".csv"):
        cargar_csv=pd.read_csv(a)
        return(cargar_csv)

#7: funciones suma,resta  
    

