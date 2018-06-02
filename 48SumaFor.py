#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:49:00 2017

@author: tizianomartinhernando
"""


suma=0
for f in range (10):
    valor=int(input('Ingrese valor: '))
    if f>4:
        suma=suma+valor
print('La suma de ultimos valores es: ')
print(suma)
