#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 20:01:12 2017

@author: tizianomartinhernando
"""
x=1
conta1=0
conta2=0
while x<=10:
    nota = int(input('Ingrese Nota: '))
    if nota>=7.:
        conta1=conta1+1
    else:
        conta2=conta2+1
    x=x+1
print('Cantidad de alumnos con notas mayores o iguales a 7: ')
print(conta1)
print('Cantidad de alumnos con notas menores a 7: ' )
print(conta2)
