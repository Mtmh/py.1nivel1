#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:58:34 2017

@author: tizianomartinhernando
"""

nombre1=input('ingrese el primer nombre: ')
nombre2=input('Ingrese el segundo nombre: ')
if nombre1==nombre2:
    print('Ingreso dos nombres iguales')
else:
    if nombre1>nombre2:
        print(nombre1)
        print('Es mayor alfabeticamente')
    else:
        print(nombre2)
        print('Es mayor alfabeticamente')
        
'''
Realizar la carga de dos nombres por teclado. Mostrar cual de los dos es mayor alfabéticamente o si son iguales.
'''
