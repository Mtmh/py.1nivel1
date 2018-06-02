#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:27:14 2017

@author: tizianomartinhernando
"""

cant1=0
cant2=0
cant3=0
cant4=0
n=int(input('Cantidad de puntos: '))
for f in range(n):
    x=int(input('ingrese coordenada x: '))
    y=int(input('Ingrese cordenada y: '))
    if x>0 and y>0:
        cant1=cant1+1
    else:
        if x<0 and y>0:
            cant2=cant2+1
        else:
            if x<0 and y <0:
                cant3=cant3+1
            else:
                if x>0 and y>0:
                    cant4=cant4+1
print('Cantidad de putos en el primer cuadarante: ')
print(cant1)
print('Cantidad de puntos en el segundo cuadarante: ')
print(cant2)
print('cantidad de puntos en el tercer cuadrante. ')
print(cant3)
print('Cantidad de puntos en el cuarto cuadrante. ')
print(cant4)

            