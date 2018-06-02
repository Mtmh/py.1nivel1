#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 13:20:05 2017

@author: tizianomartinhernando
"""

lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print(lista)

for x in range(len(lista[0])):
    if lista[0][x]>50:
        lista[0][x]=0

print(lista)

'''
Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista".
Volver a imprimir la lista.

'''
