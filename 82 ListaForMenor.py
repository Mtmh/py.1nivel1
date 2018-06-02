#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:57:13 2017

@author: tizianomartinhernando
"""

nombres=[]
for x in range(5):
    nom=input('Ingrese nombre de la persona: ')
    nombres.append(nom)

nombremenor=nombres[0]
for x in range(1,5):
    if nombres [x] < nombremenor:
        nombremenor=nombres[x]

print('La lista completa de nombres ingresado son: ')
print(nombres)
print('El nombre menor en orden alfabetico es: ')
print(nombremenor)

'''
Ingresar por teclado los nombres de 5 personas y almacenarlos
en una lista.
Mostrar el nombre de persona menor en orden alfabético.

'''
