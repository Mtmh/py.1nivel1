#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 20:46:21 2017

@author: tizianomartinhernando
"""

cantidad=0
n=int(input('Cuantos valores ingresara: '))
for f in range(n):
    valor=int(input('Ingrese valor: '))
    if valor>=1000:
        cantidad=cantidad+1
print('La cantidad de valores ingresados mayores o iguales a 1000: ')
print(cantidad)
