#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 22:39:06 2017

@author: tizianomartinhernando
"""
paises=[]
for x in range(5):
    nom=input('Ingrese el nombre del pais: ')
    paises.append(nom)
    
for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux

print('Listado de Paises: ')
print(paises)

'''

Crear una lista y almacenar los nombres de 5 países.
Ordenar alfabéticamente la lista e imprimirla.

'''
