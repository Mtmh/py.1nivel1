#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 10:40:53 2017

@author: tizianomartinhernando
"""

lista=[]
for x in range(5):
    valor=int(input('Ingrese su valor:  '))
    lista.append(valor)
    
mayor=lista[0]
for x in range (1,5):
    if lista[x]>mayor:
        mayor=lista[x]
        
print('Lista completa: ')
print(lista)
print('mayor de la lista: ')
print(mayor)

# contamos cuantas veces se encuentra el mayor en la lista
cantidad=0
for x in range (5):
    if lista [x]==mayor:
        cantidad=cantidad+1
if cantidad>1:
    print('El mayor se repite en la lista')
    

'''

Cargar una lista con 5 elementos enteros.
Imprimir el mayor un mensaje si se repite
dentro de la lista( es decir si dicho 
valor see encuentra en 2 o mas posiciones en la lista)

'''