#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:42:21 2017

@author: tizianomartinhernando
"""

mail=input('Ingrese un mail: ')
cantidad=0
x=0
while x<len(mail):
    if mail[x]=='@':
        cantidad=cantidad+1
    x=x+1
if cantidad==1:
    print('\ncontiene solo un caracter @ el mail es ingresado')
else:
    print('\nIncorrecto')
    
'''
Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@".

'''
    