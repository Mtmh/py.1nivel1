#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 20:41:02 2017

@author: tizianomartinhernando
"""

x=1
suma=0
n=int(input('Cuantas persona: '))
while x<=n:
    altura=float(input('Ingrese altura: '))
    suma=suma+altura
    x=x+1
promedio= suma / n
print('Altura promedio: ')
print(promedio)


    