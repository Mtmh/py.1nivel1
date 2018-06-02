#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 00:38:09 2017

@author: tizianomartinhernando
"""

def sumar(v1,v2,v3=0,v4=0,v5=0):
    s=v1+v2+v3+v4+v5
    return s

#bloque principal

print('\nla suma de 5 + 6: \n ')
print(sumar(5,6))
print('\nLa suma de 1 + 2 +3:\n ')
print(sumar(1,2,3))
print('\nLa suma de 1 +2 + 3 + 4 + 5:\n ')
x=sumar(1,2,3,4,5)
print(x)

'''
Confeccionar una función que reciba entre 2 y 5 enteros.
La misma nos debe retornar la suma de dichos valores.
Debe tener tres parámetros por defecto.'''
