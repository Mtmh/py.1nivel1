#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 14:09:39 2017

@author: tizianomartinhernando
"""

lista=[]
for x in range(5):
    valor=int(input('Ingrese valor: '))
    lista.append(valor)
# ordenamos de menor a mayor
for k in range(4):
    for x in range(4-k):
        if lista[x]>lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux

print('Lista de menor a mayor: ')
print(lista)

# ordenamos de mayor a menor
for k in range(4):
    for x in range(4-k):
        if lista[x]<lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux

print('Lista de mayor a menor: ')
print(lista)

'''

Cargar una lista con 5 elementos enteros.
Ordenarla de menor a mayor y mostrarla por 
pantalla, luego ordenar de mayor a menor e imprimir nuevamente.

'''