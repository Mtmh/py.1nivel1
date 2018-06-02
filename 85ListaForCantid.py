#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 12:42:30 2017

@author: tizianomartinhernando
"""

productos=[]
precios=[]
for x in range(5):
    nom=input('Ingrese el nombre del producto: ')
    productos.append(nom)
    pre=int(input('Ingrese el precio de dicho producto: '))
    precios.append(pre)

cantidad=0
for x in range(1,5):
    if precios[x]>precios[0]:
        cantidad=cantidad+1

print('Cantidad de productos con un precio mayor al primer producto ingresado: ')
print(cantidad)

'''
Crear y cargar dos listas con los nombres de 5 productos en una
y sus respectivos precios en otra. 
Definir dos listas paralelas. Mostrar cuantos productos tienen
un precio mayor al primer
producto ingresado.

'''
