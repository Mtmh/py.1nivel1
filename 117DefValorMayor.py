#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 12:11:11 2017

@author: tizianomartinhernando
"""

def mostrar_mayor(v1,v2,v3):
    print("El valor mayor de los tres numeros es el:")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)


def cargar():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    valor3=int(input("Ingrese el tercer valor:"))
    mostrar_mayor(valor1,valor2,valor3)


# programa principal

cargar()

'''
Confeccionar una función que reciba tres enteros
y nos muestre el mayor de ellos.
La carga de los valores hacerlo por teclado.
'''
