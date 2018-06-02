#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:13:29 2017

@author: tizianomartinhernando
"""

lista=[]
valor=int(input('Ingrese valor (0 para finalizar): '))
while valor!=0:
    lista.append(valor)
    valor=int(input('Ingresar valor(0 para finalizar): '))

print('Tamaño de la lista: ')
print(len(lista))

'''
Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros
al ingresar el cero. Mostrar finalmente el tamaño de la lista.

'''

