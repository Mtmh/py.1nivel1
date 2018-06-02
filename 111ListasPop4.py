#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 22:04:23 2017

@author: tizianomartinhernando
"""

lista1=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista1.append(valor)

print("Lista original")
print(lista1)

lista2=[]
posicion=0
while posicion<len(lista1):
    if lista1[posicion]>=10:
        lista2.append(lista1.pop(posicion))
    else:
        posicion=posicion+1

print("Lista despues de borrar los elementos mayores o iguales a 10")
print(lista1)
print("Lista generada con los elementos mayores o iguales a 10")
print(lista2)


'''

Crear una lista de 5 enteros y cargarlos por teclado.
Borrar los elementos mayores o iguales a 10 y generar
una nueva lista con dichos valores.

'''
