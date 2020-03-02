# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:51:32 2018

@author: DAv_O
"""

# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt

#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

#tambien importamos numpy ya que lo usamos para crear y manipular matrices
import numpy as np

from skimage import io

#tamaño de las matrices a visualizar
size=(20,30)

imagen_negra = np.zeros(size)
imagen_blanca = np.ones(size)
imagen_gris = np.ones(size)*0.5
imagen_aleatoria = np.random.rand(size[0],size[1])
imagen_cargada = io.imread("Skull.jpg")/255.0 


# imread lee las imagenes con los pixeles codificados como enteros 
# en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1
plt.figure()

print("- Dimensiones de la imagen:")
print(imagen_cargada.shape)
#plt.imshow(imagen_cargada,vmin=0,vmax=1)


imgarr = np.array(imagen_cargada)

print("- Matriz Asociada:")
print(imgarr)
print(imgarr.ndim)
