#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 19:49:34 2017

@author: tizianomartinhernando
"""

def mascaracteres(palabras):
    pos=0
    for x in range(len(palabras)):
        if len(palabras[x])>len(palabras[pos]):
            pos=x
    return palabras[pos]


# bloque principal

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))

'''
Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))'''
