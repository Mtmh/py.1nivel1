#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:02:24 2017

@author: tizianomartinhernando
"""

'''
Confeccionar una función que reciba una cadena de caracteres
 y nos devuelva los dos primeros.
En el bloque principal del programa definir una tupla
 con los nombres de meses. Mostrar por pantalla los primeros
 tres caracteres de cada mes.'''

def primeros_tres(cadena):
    return cadena[:3];


# bloque principal

meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
for x in meses:
    print(primeros_tres(x))
