#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 22:53:59 2017

@author: tizianomartinhernando
"""

def calcular_cuadrado():
    valor=int(input("Ingrese un entero:"))
    cuadrado=valor*valor
    print("El cuadrado es",cuadrado)


def calcular_producto():
    valor1=int(input("Ingrese primer valor:"))
    valor2=int(input("Ingrese segundo valor:"))
    producto=valor1*valor2
    print("El producto de los valores es:",producto)


# bloque principal

calcular_cuadrado()
calcular_producto()

'''
Desarrollar un programa con dos funciones.
La primer solicite el ingreso de un entero y muestre el cuadrado
de dicho valor. La segunda que solicite la carga de dos valores
y muestre el producto de los mismos. 
LLamar desde el bloque del programa principal a ambas funciones.

'''
