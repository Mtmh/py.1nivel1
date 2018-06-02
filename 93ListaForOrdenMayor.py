#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:11:20 2017

@author: tizianomartinhernando
"""

alumnos=[]
notas=[]
for x in range(5):
    nom=input('Ingrese el nombre del alumno: ')
    alumnos.append(nom)
    no=int(input('Ingrese Nota de dicho alumno: '))
    notas.append(no)

for k in range(4):
    for x in range(4):
        if notas[x]<notas[x+1]:
            aux1=notas[x]
            notas[x]=notas[x+1]
            notas[x+1]=aux1
            aux2=alumnos[x]
            alumnos[x]=alumnos[x+1]
            alumnos[x+1]=aux2
            
print('Lista de alumnos y sus notas ordenadas de mayor a menor: ')
for x in range(5):
    print(alumnos[x],notas[x])
    

'''
Confeccionar un programa que permita cargar los nombres
 de 5 alumnos y sus notas respectivas. Luego ordenar las
 notas de
 mayor a menor.
 Imprimir las notas y los nombres de los alumnos.
 
'''
