#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 20:34:56 2017

@author: tizianomartinhernando
"""

'''
Confeccionar una programa con las siguientes funciones:
1) Generar una lista con 5 elementos enteros aleatorios
  comprendidos entre 1 y 3.
2) Controlar que el primer elemento de la lista sea un 1,
  en el caso que haya un 2 o 3 mezclar la lista y 
  volver a controlar hasta que haya un 1. 
3) Imprimir la lista'''
    


import random

def cargar():
    lista=[]
    for x in range(5):
        lista.append(random.randint(1,3))
    return lista

def controlar_primero(lista):
    while lista[0]==1:
        random.shuffle(lista)
        

def imprimir(lista):
    print(lista)
    

# bloque principal
    

lista= cargar()
imprimir(lista)
controlar_primero(lista)
imprimir(lista)


    