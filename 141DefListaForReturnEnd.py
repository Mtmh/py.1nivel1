#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:45:58 2017

@author: tizianomartinhernando
"""

def cargar():
    lista=[]
    for x in range(10):
        valor=int(input('Ingrese valor: '))
        lista.append(valor)
    return lista

def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x], end=',')
        
# bloque principal
        
lista=cargar()
imprimir(lista)

'''
Cargar una lista de 10 enteros, luego mostrarlos por pantalla
 a cada elemento separados por una coma.'''
 
 