#taller pre quiz 2
import numpy as np 
import matplotlib as plt

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