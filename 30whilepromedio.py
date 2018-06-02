#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 00:14:41 2017

@author: tizianomartinhernando
"""

x=1
suma=0
while x<=10:
    valor=int(input('Ingrese un valor: '))
    suma=suma+valor
    x=x+1
promedio=suma/10
print('La suma de los 10 valores es: ')
print(suma)
print('El promedio es: ')
print(promedio)
