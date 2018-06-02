#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:14:40 2017

@author: tizianomartinhernando
"""

'''
Cargar una cadena por teclado luego:
1) Imprimir los dos primeros caracteres.
2) Imprimir los dos últimos
3) Imprimir todos menos el primero y el último caracter.'''
    

    
cadena=input("Ingrese una cadena de caracteres:")
print("Los dos primeros caracteres")
print(cadena[:2])
print("Los dos ultimos caracteres")
print(cadena[len(cadena)-2:])
print("Todos los caracteres menos el primero y el ultimo")
print(cadena[1:len(cadena)-1])