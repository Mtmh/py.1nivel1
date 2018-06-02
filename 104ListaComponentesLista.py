#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 12:39:22 2017

@author: tizianomartinhernando
"""

padres=[]
hijos=[]
for k in range(3):
    pa=input("Ingrese el nombre del padre:")
    ma=input("Ingrese el nombre del hijo:")    
    padres.append([pa, ma])
    cant=int(input("Cuantos hijos tienen esta familia:"))
    hijos.append([])
    for x in range(cant):
        nom=input("Ingrese el nombre del hijo:")
        hijos[k].append(nom)

print("Listado del padre, madre y sus hijos")
for k in range(3):
    print("Padre:",padres[x][0])
    print("Madre:",padres[x][1])
    for x in range(len(hijos[k])):
        print("Hijo:",hijos[k][x])

print("Listado del padre y cantidad de hijos que tiene")
for x in range(3):
    print("padre:",padres[x][0])
    print("Cantidad de hijos:",len(hijos[x]))
    
'''
Definir dos listas de 3 elementos.
La primer lista cada elemento es una sublista con el nombre del padre y la madre de una familia.
La segunda lista está constituida por listas con los nombres de los hijos de cada familia. Puede haber familias sin hijos.
Imprimir los nombres de del padre, la madre y sus hijos.
También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.
Un ejemplo si se define por asignación:
padres=[["juan","ana"], ["carlos","maria"], ["pedro","laura"]]
hijos=[["marcos","alberto","silvia"], [], ["oscar"]]
Como son listas paralelas podemos decir que la familia cuyos padres son "juan" y "ana" tiene tres hijos llamados "marcos", "alberto", "silvia". La segunda familia no tiene hijos y la tercera tiene solo uno.

'''
