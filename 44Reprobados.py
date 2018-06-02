#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 20:34:42 2017

@author: tizianomartinhernando
"""

aprobados=0
reprobados=0
for f in range(10):
    nota=int(input('Ingrese la nota: '))
    if nota>=7:
        aprobados=aprobados+1
    else:
        reprobados=reprobados+1
print('Cantidad de aprobados: ')
print(aprobados)
print('Cantidad de reprobados: ')
print(reprobados)
