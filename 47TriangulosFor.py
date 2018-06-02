#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:41:47 2017

@author: tizianomartinhernando
"""

n=int(input('Cuantos triangulos procesara?: '))
cantidad=0
for x in range(n):
    basetri=int(input('Ingrese el valor de la base: '))
    altura=int(input('Ingrese el valor de la altura: '))
    superficie=basetri*altura/2
    print('La superficie es: ')
    print(superficie)
    if superficie>12:
        cantidad=cantidad+1
print('La cantidad de triangulos con superficie superior a 12 son: ')
print(cantidad)

    