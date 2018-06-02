#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 18:44:35 2017

@author: tizianomartinhernando
"""

def cantidad_mayores18(edad1,*edades):
    cant=0
    if edad1>=18:
        cant=cant+1
    for x in range(len(edades)):
        if edades[x]>=18:
            cant=cant+1
    return cant

# bloque principal
    
print('La cantidad de personas mayores a 18 son: ', cantidad_mayores18(23,6,8,19,24))

'''
Confeccionar una función que reciba una serie de edades
 y me retorne la cantidad que son mayores o iguales
 a 18 (como mínimo se envía un entero a la función)
 '''
 