#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 13:09:19 2017

@author: tizianomartinhernando
"""

def retornar_mayor(v1,v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
    return mayor


# bloque principal
valor1=int(input("Ingrese el primer valor:"))
valor2=int(input("Ingrese el segundo valor:"))
print(retornar_mayor(valor1,valor2))

'''Confeccionar una función que le enviemos como
parámetros dos enteros y nos retorne el mayor'''

'''
Si queremos podemos hacerla más sintética a esta función
sin tener que guardar en una variable local el valor a retornar:

    def retornar_mayor(v1,v2):
    if v1>v2:
        return v1
    else:
        return v2
        


'''