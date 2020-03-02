# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:10:25 2018

@author: DAv_O
"""

import matplotlib.pyplot as plt
plt.rcParams['image.cmap'] = 'gray' #configuracion necesaria de pyplot para ver las imagenes en escala de grises
import math
import random 
import numpy as np
import PIL 
from skimage import io



imagen2D = PIL.Image.open('Fsociety.jpg').convert('L')
imgarr = np.array(imagen2D)
f,c = imgarr.shape
matriz=[]

print("f",f)
print("c",c)
fRaiz=int(math.sqrt(f))
cRaiz=int(math.sqrt(c))


print("- Dimensiones de la imagen:",imgarr.shape)
plt.imshow(imgarr)
print("Raiz f:", fRaiz)
print("Raiz c:", cRaiz)

print("___________________________________")

print(imgarr)
print("Array Size:", imgarr.size)

print(imgarr[0:fRaiz,0:cRaiz])

print("___________________________________")


for i in range(fRaiz):
    
    for j in range(cRaiz):   
        
        fi = (fRaiz*(i+1))    
        #print("filas= ",(fRaiz*i),":",fi)
        co = (cRaiz*(j+1))
        #print("Columnas= ",(cRaiz*j),": ",co)
        matriz.append(imgarr[(fRaiz*i):fi , (cRaiz*j):co])
        #matriz[i].append(imgarr[0:fRaiz,0:cRaiz])

random.shuffle(matriz)
#print(matriz)






