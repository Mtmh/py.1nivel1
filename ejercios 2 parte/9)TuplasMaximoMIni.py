#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:54:48 2017

@author: tizianomartinhernando
"""
'''
Crea una tupla con números e indica el numero con mayor valor
 y el que menor tenga'''
'''
numeros = (5,4,3,-2,1,6,455,3,6,6,6,6,6)
 
maximo = numeros[0]
minimo = numeros[0]
 
for i in numeros:
    if i > maximo:
        maximo = i
 
    if i &lt; minimo:
        minimo = i
 
print("El maximo es ",maximo)
print("El minimo es ",minimo)'''

numeros = (7,6,5,4,3,2,3,4,5,1,4,3)
 
print("Maximo: ",max(numeros))
 
print("Minimo: ",min(numeros))