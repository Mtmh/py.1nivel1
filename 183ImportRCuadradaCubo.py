#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 18:19:19 2017

@author: tizianomartinhernando
"""

'''
Confeccionar un programa que solicite la carga de un valor
 entero por teclado y luego nos muestre la raíz cuadrada
 del número y el valor elevado al cubo'''
 

from math import sqrt, pow

valor=int(input('Ingrese un valor entero: '))
r1=sqrt(valor)
r2=pow(valor,3)
print('La raiz cuadrada es: ',r1)
print('El cubo es: ',r2)

