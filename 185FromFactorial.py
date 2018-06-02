#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 18:28:50 2017

@author: tizianomartinhernando
"""

'''
Calcular el factorial de un número ingresado por teclado.
El factorial de un número es la cantidad que resulta de 
la multiplicación de determinado número natural
 por todos los números naturales que le anteceden
 excluyendo el cero. 
 Por ejemplo el factorial de 4 es 24, que resulta de 
 multiplicar 4*3*2*1.
No hay que implementar el algoritmo para calcular el factorial
 sino hay que importar dicha funcionalidad del módulo math.
El módulo math tiene una función llamada factorial
 que recibe como parámetro un entero del que necesitamos
 que nos retorne el factorial.
Solo importar la funcionalidad factorial del módulo
 math de la biblioteca estándar de Python.'''
 
from math import factorial

valor=int(input('Ingrese un valor: '))
resu=factorial(valor)
print('El Factorial de', valor,'es: ',resu)
