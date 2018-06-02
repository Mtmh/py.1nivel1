c#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 15:41:27 2017

@author: tizianomartinhernando
"""
'''
Crear y cargar una lista con los nombres de tres alumnos.
Cada alumno tiene dos notas, almacenar las notas en una 
lista paralela.
Cada componente de la lista paralela debe ser también una lista 
con las dos notas. Imprimir luego cada nombre y sus dos notas.
'''
nombres=[]
notas=[]
for x in range(3):
    nom=input("Ingrese el nombre del alumno:")
    nombres.append(nom)
    no1=float(input("Ingrese la primer nota:"))
    no2=float(input("Ingrese la segunda nota:"))
    notas.append([no1,no2])

for x in range(3):
    print(nombres[x],notas[x][0],notas[x][1])
    
    