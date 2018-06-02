#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:45:52 2017

@author: tizianomartinhernando
"""

'''
Cargar una cadena de caracteres por teclado.
 Mostrar la cadena del final al principio utilizando
 subíndices negativos.'''
 
palabra=input('Ingresar palabra: ')
indice=-1
for x in range(len(palabra)):
    print(palabra[indice],end='')
    indice=indice-1
    