#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 12:21:28 2017

@author: tizianomartinhernando
"""

def mostrar_perimetro(lado):
    per=lado*4
    print("El perimetro es",per)


def mostrar_superficie(lado):
    sup=lado*lado
    print("La superficie es",sup)


def cargar_dato():
    la=int(input("Ingrese el valor del lado de un cuadrado:"))
    respuesta=input("Quiere calcular el perimetro o la superficie[ingresar texto: perimetro/superficie]?")
    if respuesta=="perimetro":
        mostrar_perimetro(la)
    if respuesta=="superficie":
        mostrar_superficie(la)


# programa principal

cargar_dato()

'''
Desarrollar un programa que permita ingresar el lado de un cuadrado.
Luego preguntar si quiere calcular y mostrar su perímetro
o su superficie.
'''
