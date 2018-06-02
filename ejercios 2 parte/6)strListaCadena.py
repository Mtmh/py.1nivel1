#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:33:14 2017

@author: tizianomartinhernando
"""

'''
Pide una cadena por teclado, mete los caracteres
 en una lista sin espacios.'''
 
'''lista=[]

cadena=str(input('Ingrese cadena: '))

lista.append(cadena)

print(cadena)'''

cadena=input('Dame una cadena: ')
print(cadena)
lista=[]
for c in cadena:
    if(c != ' '):
        lista.append(c)
print(lista)#No es mia




