#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 13:46:43 2017

@author: tizianomartinhernando
"""

cantidad=int(input("Cuantos empleados tiene la empresa?: "))
sueldos=[]
for x in range(cantidad):
    su=int(input("Ingrese sueldo: "))
    sueldos.append(su)

# ordenamos la lista
for k in range(cantidad-1):
    for x in range(cantidad-1-k):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print("Lista de sueldos ordenados")
print(sueldos)

'''

Solicitar por teclado la cantidad de empleados
que tiene la empresa. Crear y cargar una lista con todos
los sueldos de dichos empleados. Imprimir la lista de sueldos.

'''
