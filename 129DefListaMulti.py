#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 19:40:10 2017

@author: tizianomartinhernando
"""

def multiplicar(lista,va):
    for x in range(len(lista)):
        multi=lista[x]*va
        print(multi)


# bloque principal

lista=[3, 7, 8, 10, 2]
print("Lista original:",lista)
print("Lista multiplicando cada elemento por 3")
multiplicar(lista,3)

'''
Crear una lista de enteros por asignación. 
Definir una función que reciba una lista de enteros y un segundo
parámetro de tipo entero. 
Dentro de la función mostrar cada elemento de la lista 
multiplicado por el valor entero enviado.
lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)

'''
