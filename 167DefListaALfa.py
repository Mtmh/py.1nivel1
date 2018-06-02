#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 23:33:41 2017

@author: tizianomartinhernando
"""

'''
Confeccionar un programa que contenga
 las siguientes funciones:
     
1) Carga de una lista de 5 nombres.
2) Ordenar alfabéticamente la lista.
3) Imprimir la lista de nombres'''
    
def cargar():
    nombres=[]
    for x in range(5):
        nom=input('Ingrese nombre: ')
        nombres.append(nom)
    return nombres

def ordenar(nombres):
    for k in range(4):
        for x in range(4):
            if nombres[x]>nombres[x+1]:
                aux=nombres[x]
                nombres[x]=nombres[x+1]
                nombres[x+1]=aux

def imprimir(nombres):
    for x in range(len(nombres)):
        print(nombres[x],' ',end='')

# bloque principal
        
nombres=cargar()
ordenar(nombres)
imprimir(nombres)

