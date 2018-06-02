#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 20:16:23 2017

@author: tizianomartinhernando
"""

'''
Desarrollar un programa que cargue una lista con 10 enteros.
Cargar los valores aleatorios 
con números enteros comprendidos entre 0 y 1000.
Mostrar la lista por pantalla.
Luego mezclar los elementos de la lista y volver a mostrarlo.'''


import random

def cargar():
    lista=[]
    for x in range(10):
        lista.append(random.randint(0,1000))
    return lista

def imprimir(lista):
    print(lista)
    

def mezclar(lista):
    random.shuffle(lista)
    
# bloque principal
    
lista=cargar()
print('Lista generada aleatoriamente: ')
imprimir(lista)
mezclar(lista)
print('La misma lista luego despues de mezclar: ')
print(lista)

