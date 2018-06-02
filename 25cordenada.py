#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 23:37:44 2017

@author: tizianomartinhernando
"""

print('Ingrese Cordenada: ')
x = int(input('Ingrese coordenada x: '))
y = int(input('Ingrese cordenada y: '))
if x>0 and y>0:
    print('Se encuentra en el primer cuadrante')
else:
    if x<0 and y<0:
        print('Se encuentra en el tercer cuadrante')
    else:
        print('Se encuentra en el cuarto cuadrante')
