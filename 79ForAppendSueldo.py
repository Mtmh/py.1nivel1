#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 23:43:01 2017

@author: tizianomartinhernando
"""

sueldosmañ=[]
print('Sueldos turno mañana')
for x in range(4):
    valor=float(input('Ingrese sueldo: '))
    sueldosmañ.append(valor)

sueldostar=[]
print('Sueldos turno tarde')
for x in range(4):
    valor=float(input('Ingrese sueldo: '))
    sueldostar.append(valor)

print('Turno de mañana: ')
print(sueldosmañ)
print('Turno tarde: ')
print(sueldostar)

'''

Una empresa tiene dos turnos (mañana y tarde)
en los que trabajan 8 empleados
(4 por la mañana y 4 por la tarde)
Confeccionar un programa que permita almacenar
los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.

'''
