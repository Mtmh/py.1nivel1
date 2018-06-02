#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:59:51 2017

@author: tizianomartinhernando
"""
'''definimos tres contadores
que se muestran distintos a cero'''
suma1=0
suma2=0
suma3=0

for f in range(5):
    edad=int(input('Ingrese Edad: '))
    suma1=suma1+edad
pro1=suma1/5
print('Promedio de edades de turno de mañana: ')
print(pro1)

for f in range(6):
    edad=int(input('Ingrese Edad. '))
    suma2=suma2+edad
pro2=suma2/6
print('Promedio de edades del turno de tarde: ')
print(pro2)

for f in range(11):
    edad=int(input('Ingrese Edad: '))
    suma3=suma3+edad
pro3=suma3/11
print(pro3)
if pro1<pro2 and pro1<pro3:
    print('El turno de mañana tiene un promedio menor de edades')
else:
    if pro2<pro3:
        print('El turno de tarde tiene un promedio menor de edades.')
    else:
        print('El turno de noche tiene un promedio menor de edades.')
        
        
    