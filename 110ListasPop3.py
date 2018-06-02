#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:06:57 2017

@author: tizianomartinhernando
"""

empleados=[]
sueldos=[]
cant=int(input("Cuantos empleados tiene la empresa:"))
for x in range(cant):
    nom=input("Ingrese el nombre:")
    empleados.append(nom)
    su=int(input("Ingrese el importe del sueldo:"))
    sueldos.append(su)

print("Listado completo de empleados")
for x in range(len(sueldos)):
    print(empleados[x],sueldos[x])

posicion=0
while posicion<len(sueldos):
    if sueldos[posicion]>10000:
        sueldos.pop(posicion)
        empleados.pop(posicion)
    else:
        posicion=posicion+1

print("Listado de empleados que cobran 10000 o menos")
for x in range(len(sueldos)):
    print(empleados[x],sueldos[x])


'''

Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)

'''
