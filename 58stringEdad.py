#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:17:06 2017

@author: tizianomartinhernando
"""

print('\nDatos de la primera persona: ')
nombre1=input('Ingrese nombre: ')
edad1=int(input('Ingrese la edad: '))
altura1=float(input('Ingrese la altura Ej: 1.75: '))
print('\nDatos de la segunda persona:\n ')
nombre2=input('ingrese Nombre: ')
edad2=int(input('Ingrese Edad: '))
altura2=float(input('Ingrese la altura Ej: 1.75: '))
print('\nLa persona mas alta es:\n ')
if altura1>altura2:
    print(nombre1)
elif altura1<altura2:
    print(nombre2)
elif altura1==altura2:
    print('Son iguales')
else:
    print('Que diferentes son')
print('\nLa persona mas joven es:\n ')
if edad1<edad2:
    print(nombre1)
else:
    print(nombre2)

'''  Realizar la carga por teclado del nombre, edad y altura de dos personas. Mostrar por pantalla el nombre de la persona con mayor altura.'''

'''  
print("Datos de la primer persona")
nombre1=input("Ingrese nombre:")
edad1=int(input("Ingrese la edad:"))
altura1=float(input("Ingrese la altura Ej 1.75:"))
print("Datos de la segunda persona")
nombre2=input("Ingrese nombre:")
edad2=int(input("Ingrese la edad:"))
altura2=float(input("Ingrese la altura Ej 1.75:"))
print("La persona mas alta es:")
if altura1>altura2:
    print(nombre1)
else:
    print(nombre2)
'''
