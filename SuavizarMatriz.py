# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 12:51:33 2018

@author: Estudiantes
"""

import numpy as np

l = np.arange(16).reshape(4,4)
n = np.random.random((30,30))*10
m = np.zeros((4,4))


for i in range(0,4):
    for j in range(0,4):
        aux= l[i][j]
        print("____________________")
        
        for a in range(0,3):
            
            for b in range(0,3):

                print("i:",i," j:",j)
                print("aux:",aux)
                print("a:", a-1," b:",b-1)
                print("->",l[a-1][b-1])
                
                aux= aux + l[a-1][b-1]

                print("suma:",aux)
                
                m[i][j]= aux   
                             

      
                      
print(l)
print(m)
