#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:23:22 2017

@author: tizianomartinhernando
"""
sueldos=[]
suma=0
for x in range(5):
    valor=float(input('Ingrese el sueldo del operario: '))
    sueldos.append(valor)
    suma=suma+valor
print('Lisa de sueldos: ')
print(sueldos)
promedio=suma/5
print('Promedio de sueldos: ')
print(promedio)

'''
Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.

'''