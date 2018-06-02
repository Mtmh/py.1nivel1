#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 19:54:51 2017

@author: tizianomartinhernando
"""

cantidad=0
x=1
n=int(input('Cuangas piezas cargara: '))
while x<=n:
    largo=float(input('ingrese la medida de la pieza: '))
    if largo>= 1.2 and largo<=1.3:
        cantidad=cantidad+1
    x=x+1
print('Lacantidad de piezas aptas son: ')
print(cantidad)
