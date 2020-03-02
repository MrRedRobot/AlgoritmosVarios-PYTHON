# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:51:32 2018

@author: DAv_O
"""

# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import math
import random 

#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

#tambien importamos numpy ya que lo usamos para crear y manipular matrices
import numpy as np

import PIL 
from skimage import io

#tamaño de las matrices a visualizar
size=(20,30)

imagen_negra = np.zeros(size)
imagen_blanca = np.ones(size)
imagen_gris = np.ones(size)*0.5
imagen_aleatoria = np.random.rand(size[0],size[1])
imagen_cargada = io.imread("skull.jpg")/255.0 


# imread lee las imagenes con los pixeles codificados como enteros 
# en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1
plt.figure()


imagen2D = PIL.Image.open('Fsociety.jpg').convert('L')
imgarr = np.array(imagen2D)


print("- Dimensiones de la imagen:",imgarr.shape)
plt.imshow(imgarr)

#print("- Matriz Asociada:")
#print(imgarr)
#print(imgarr.ndim)

f,c = imgarr.shape


print("f",f)
print("c",c)


print(imgarr)
print("Size:", imgarr.size)

print("___________________________________")

random.shuffle(imgarr)
print(imgarr)

print("___________________________________")

fRaiz=int(math.sqrt(f))
cRaiz=int(math.sqrt(c))
#n=imgarr.reshape(int(fRaiz),int(cRaiz))

print("___________________________________")
print(imgarr[0:fRaiz,0:cRaiz])
plt.imshow(imgarr[0:fRaiz,0:cRaiz])
plt.title("parte")
plt.figure()


my_list = list()
my_list.append(imgarr[0:fRaiz,0:cRaiz])
my_list.append(imgarr[fRaiz:fRaiz*2, cRaiz:cRaiz*2])
my_list.append(imgarr[fRaiz*2:fRaiz*3, cRaiz*2:cRaiz*3])
my_list.append(imgarr[fRaiz*3:fRaiz*4, cRaiz*3:cRaiz*4])
my_list.append(imgarr[fRaiz*4:fRaiz*5, cRaiz*4:cRaiz*5])
my_list.append(imgarr[fRaiz*5:fRaiz*6, cRaiz*5:cRaiz*6])
my_list.append(imgarr[fRaiz*6:fRaiz*7, cRaiz*6:cRaiz*7])
my_list.append(imgarr[fRaiz*7:fRaiz*8, cRaiz*7:cRaiz*8])
my_list.append(imgarr[fRaiz*8:fRaiz*9, cRaiz*8:cRaiz*9])


#print(my_list)

random.shuffle(my_list)
print("___________________________________")


myarray = np.asarray(my_list)
print("_:",myarray.size)


#plt.imshow(myarray)
#plt.title("desorden? ")
#plt.figure()


n= myarray.resize(f,c)
print(myarray)
print("___________________________________")
print(n)

#for x in range(0,f):
    #for y in range(0,c):
        #print("x",x,"y",y)
        
        
        
        
        




print("___________________________________")
o = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
random.shuffle(o)

l = np.arange(900).reshape(30,30)

print(o)
o= o.reshape(3,3)
print(o)

print(l[0:4, 0:4])



    
#m = np.zeros(c,f)

#Filtro 1

#plt.imshow(m)