#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 22:35:42 2017

@author: tizianomartinhernando
"""

n=int(input('Cuantos empleados tiene la empresa: '))
x=1
conta1=0
conta2=0
gastos=0
while x<=n:
    sueldo=float(input('ingrese el sueldo del empleado: '))
    if sueldo<=300:
        conta1=conta1+1
    else:
        conta2=conta2+1
        gastos=gastos+sueldo
        x=x+1
print('Cantidad de empleados con sueldos entre 100 y 300:  ')
print(conta1)
print('Cantidad de empleados con sueldos mayor a 300: ')
print(conta2)
print('Gastostotal de la empresa en sueldos: ')
print(gastos)

