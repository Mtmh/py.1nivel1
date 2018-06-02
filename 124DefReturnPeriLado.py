#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 16:55:56 2017

@author: tizianomartinhernando
"""

def retornar_perimetro(lado):
    perimetro=lado*4
    return perimetro


# bloque principal

lado=int(input("Lado del cuadrado:"))
print("El perimetro es:",retornar_perimetro(lado))

'''
Elaborar una función que nos retorne el perímetro de un cuadrado
 pasando como parámetros el valor de un lado.
 
'''
