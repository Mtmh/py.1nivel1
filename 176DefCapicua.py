#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:37:29 2017

@author: tizianomartinhernando
"""
'''
Confeccionar una función que reciba una palabra
y verifique si es capicúa (es decir que se lee
 igual de izquierda a derecha que de derecha a izquierda)'''


def capicua(cadena):
    indice=-1
    iguales=0
    for x in range(0,len(cadena)//2):
        if cadena[x]==cadena[indice]:
            iguales=iguales+1
        indice=indice-1
    print(cadena)
    if iguales==(len(cadena)//2):
        print('Es capicua')
    else:
        print('No es capicua')
#bloque principal
        
capicua('Neuquen')
capicua('Casa')

