#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 19:39:56 2017

@author: tizianomartinhernando
"""

def cargar_sueldos():
    sueldos=[]
    for x in range(10):
        su=int(input('Ingrese sueldo:\n '))
        sueldos.append(su)
    return sueldos

def imprimir_sueldos(sueldos):
    print('Listado de sueldos')
    for x in range(len(sueldos)):
        print(sueldos[x])

def sueldos_mayor4000(sueldos):
    cant=0
    for x in range(len(sueldos)):
        if sueldos[x]>4000:
            cant=cant+1
    print('Cantidad de empleados con un sueldo superior a 4000: ',cant)

def promedio(sueldos):
    suma=0
    for x in range(len(sueldos)):
        suma=suma+sueldos[x]
    promedio=suma//10
    return promedio

def sueldos_bajos(sueldos):
    pro=promedio(sueldos)
    print('Sueldo promedio de la empresa: ', pro)
    print('Sueldos in feriores al promedio: ')
    for x in range(len(sueldos)):
        if sueldos[x]<pro:
            print(sueldos[x])

def sueldos_mayores(sueldos):# Indentado por mi no por tutorial
    pro=promedio(sueldos)
    print('Sueldos mayores al promedio: ')
    for x in range(len(sueldos)):
        if sueldos[x]>pro:
            print(sueldos[x])
            
                
# bloque principal

sueldos=cargar_sueldos()
imprimir_sueldos(sueldos)
sueldos_mayor4000(sueldos)
sueldos_mayores(sueldos)# No original ingresado por mi 
sueldos_bajos(sueldos)

'''
Desarrollar una aplicación que permita ingresar por teclado
 los nombres de 5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de articulos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y
luego mostrar todos los artículos con un precio menor igual
al valor ingresado.'''


