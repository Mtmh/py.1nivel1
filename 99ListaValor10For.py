#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 13:21:51 2017

@author: tizianomartinhernando
"""

lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

print(lista)

for k in range(len(lista)):
    for x in range(len(lista[k])):
        if lista[k][x]>10:
            lista[k][x]=0
print(lista)

            
'''
Se tiene la siguiente lista:
lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos 
los elementos mayores a 10 contenidos en todos los 
elementos de la variable "lista".
Volver a imprimir la lista.

'''
