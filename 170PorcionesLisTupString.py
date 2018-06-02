#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 18:52:17 2017

@author: tizianomartinhernando
"""

'''
El lenguaje Python nos facilita una sintaxis muy sencilla
 par recuperar un trozo de una lista, tupla o cadena 
 de caracteres.'''

lista1=[0,1,2,3,4,5,6]
lista2=lista1[2:5]
print(lista2) # 2,3,4
lista3=lista1[1:3]
print(lista3) # 1,2
lista4=lista1[:3]
print(lista4) # 0,1,2
lista5=lista1[2:]
print(lista5) # 2,3,4,5,6