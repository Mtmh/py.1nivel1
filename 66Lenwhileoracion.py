#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:59:25 2017

@author: tizianomartinhernando
"""

oracion=input('Ingrese su oracion: ')
cantidad=0
x=0
while x<len(oracion):
    if oracion[x]==' ':
        cantidad=cantidad+1
    x=x+1
print('la cantidad de espacios en blanco ingresado son: ')
print(cantidad)
