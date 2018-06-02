#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:49:53 2017

@author: tizianomartinhernando
"""

'''
Confeccionar un programa con las siguientes funciones:
1) Cargar una lista con 5 palabras.
2) Intercambiar la primer palabra con la última.
3) Imprimir la lista'''
    
def cargar():
    palabras=[]
    for x in range(0,5):
        pal=input('Ingrese una palabra: ' ' ')
        palabras.append(pal)
    return palabras

def intercambiar(palabras):
    aux=palabras[0]
    palabras[0]=palabras[-1]
    palabras[-1]=aux
    
def imprimir(palabras):
    print(('\n'),palabras,('\n'))
        
    
    
## bloque principal
    
palabras=cargar()
imprimir(palabras)
intercambiar(palabras)
imprimir(palabras)
