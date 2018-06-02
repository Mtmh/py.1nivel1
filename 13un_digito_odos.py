#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 23:42:54 2017

@author: tizianomartinhernando
"""

print('Ingrese un numero de uno o dos digitos: ')
num = int(input('Ingrese el primer valor: '))
if num <10:
    print('\nUn digito igresado')
else:
    if num <100:
        print('\nDos digitos ingresados')
    else:
        print('\nError de entrada de datos')
        