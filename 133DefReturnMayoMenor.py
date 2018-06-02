#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 18:47:38 2017

@author: tizianomartinhernando
"""
'''
Confeccionar una función que cargue por teclado una lista de 5 enteros
y la retorne.
 Una segunda función debe recibir una lista
 y retornar el mayor y el menor valor de la lista.
 Desde el bloque principal del programa llamar a
 ambas funciones e imprimir el mayor y el menor de la lista'''




def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li


def retornar_mayormenor(li):
    ma=li[0]
    me=li[0]
    for x in range(1,len(li)):
        if li[x]>ma:
            ma=li[x]
        else:
            if li[x]<me:
                me=li[x]
    return [ma,me]                


# bloque principal del programa

lista=carga_lista()
mayor, menor=retornar_mayormenor(lista)
print("Mayor elemento de la lista:", mayor)
print("Menor elemento de la lista:", menor)

