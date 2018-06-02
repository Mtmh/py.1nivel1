#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 13:40:18 2017

@author: tizianomartinhernando
"""

lista=[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]

suma=0
for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]
print(suma)

'''

Crear una lista por asignación. La lista tiene que tener 5 elementos. Cada elemento debe ser una lista, la primera lista tiene que tener un elemento, la segunda dos elementos, la tercera tres elementos y así sucesivamente.
Sumar todos los valores de las listas.

'''
