# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 13:24:04 2018

@author: Estudiantes
"""
"""
Editor de Spyder

Este es un archivo temporal
"""
from random import randint



def generarAleatorio():
    return (randint(0,99))

def leerPrediccion():
    print("____________________")
    print("Digite su prediccion")
    return (int(input()))

def juego(aleatorio,apuesta):
    
    puntaje=10
    
    while puntaje>0:

        print("Intentos restantes:" ,puntaje)
        
        if aleatorio == apuesta:
            print("Felicitaciones!!!" , aleatorio )
            print("Puntaje:", puntaje)
            break
        
        if aleatorio < apuesta:
            print("Su Prediccion es demasiado alta")
            apuesta= leerPrediccion()
            puntaje   -= 1
            
        if aleatorio > apuesta:
            print("Su Prediccion es demasiado baja")  
            apuesta= leerPrediccion()
            puntaje  -= 1
        
    else:
        print("Fin Del Juego")
        print("Puntaje:" , puntaje)
        

prediccion= leerPrediccion()
aleatorio = generarAleatorio()
print(aleatorio)
juego(aleatorio,prediccion)
