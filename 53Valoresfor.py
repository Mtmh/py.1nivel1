#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:43:09 2017

@author: tizianomartinhernando
"""
negativos=0
positivos=0
mult15=0
sumapares=0
for x in range(10):
    valor=int(input('Ingrese valor: '))
    if valor<0:
        negativos=negativos+1
    else:
        if valor>0:
            positivos=positivos+1
    if valor%15==0:
        mul15=mult15+1
    if valor%2==0:
        sumapares=sumapares+valor
print('Cantidad de valores negativos: ')
print(negativos)
print('Cantidad de valores positivos: ')
print(positivos)
print('Cantidad de valores multiplos de 15: ')
print(mult15)
print('Suma de los valores pares: ')
print(sumapares)

    
    