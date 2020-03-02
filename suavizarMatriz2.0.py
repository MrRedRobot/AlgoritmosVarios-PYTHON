# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 12:40:34 2018

@author: Estudiantes
"""

import numpy as np

l = np.arange(900).reshape(30,30)
n = np.random.random((30,30))*10
m = np.zeros((30,30))


for x in range(0,30):
    for y in range(0,30):
        
        if x==29:
            i=0
        else:
            i=x-1
        if y==29:
            j=0
        else:
            j=y-1
               
        m[x][y]= (l[i][j] + l[i-1][j-1] + l[i-1][j] + l[i-1][i+1] + l[i][j-1] + l[i][j+1] + l[i+1][j+1] + l[i+1][j] + l[i+1][j+1])/9     
                        
        print("____________________")
        
        print("x:",x," y:",y)
        print("aux:",m[x][y])
        print("i:", i," j:",j)
        print("->",l[i][j])             
                        

      
                      
print(l)
print(m)