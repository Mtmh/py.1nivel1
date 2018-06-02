#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 20:39:39 2017

@author: tizianomartinhernando
"""

mul3=0
mul5=0
for f in range(10):
    valor=int(input('Ingrese un valor: '))
    if valor%3==0:
        mul3=mul3+1
    if valor%5==0:
        mul5=mul5+1
print('Cantidad de valores ingresados multiplos de 3: ')
print(mul3)
print('Cantidad de valores ingresados multiplos de 5: ')
print(mul5)
