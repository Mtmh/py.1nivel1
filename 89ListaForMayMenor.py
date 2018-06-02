#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 22:33:02 2017

@author: tizianomartinhernando
"""

sueldos=[]
for x in range(5):
    valor=int(input('Ingrese sueldo: '))
    sueldos.append(valor)
    
print('Lista sin ordenar: ')
print(sueldos)

for k in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux
            
print('Lista ordenada: ')
print(sueldos)

'''

Se debe crear y cargar una lista donde
almacenar 5 sueldos. Ordenar de menor a mayor la lista.

'''

'''

Si bien el algoritmo planteado funciona, un algoritmo más eficiente, que se deriva del anterior es el plantear un for interno con la siguiente estructura:
for k in range(4):
    for x in range(4-k):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux
Es decir restarle el valor del contador del for externo.

'''
