#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:21:40 2017

@author: tizianomartinhernando
"""

lista1=[]
print('Carga de la primera lista: ')
for x in range(4):
    valor=int(input('Ingrese valor: '))
    lista1.append(valor)

lista2=[]
print('Carga la segunda lista: ')
for x in range(4):
    valor=int(input('Ingrese valor: '))
    lista2.append(valor)
    
listasuma=[]
for x in range(4):
    suma=lista1[x]+lista2[x]
    listasuma.append(suma)
    
print('Lista resultante: ')
print(listasuma)

'''

Realizar un programa que pida la carga de dos listas
numéricas enteras de 4 elementos cada una.
Generar una tercer lista que surja de la suma de los elementos
de la misma posición de cada lista. Mostrar esta tercer lista.

'''
