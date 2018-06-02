#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 23:07:09 2017

@author: tizianomartinhernando
"""

x=1
pares=0
impares=0
n=int(input('Cuantos numeros ingresara?: '))
while x<=n:
    valor=int(input('Ingrese el valor'))
    if valor%2==0:
        pares=pares+1
    else:
        impares=impares+1
    x=x+1
print('Cantidad de pares: ')
print(pares)
print('Cantidad de impares: ')
print(impares)
