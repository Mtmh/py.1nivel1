#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:49:45 2017

@author: tizianomartinhernando
"""

print ("Programa para multiplicar, Suma, Resta, Division")
 
print ("Selecciona un numero\n 1. Suma\n 2. Resta\n 3. Multiplicacion\n 4. Division\n")
 
opcion = input()
#while (opcion <=4):
    if opcion == 1:
        print "Suma"
        x = input("Primer numero: ")
        y = input ("Segundo numero: ")
        suma = int(x + y)
        print x, "+", y, "=", suma
 
    elif opcion == 2:
        print "Resta"
        x = input("Primer numero: ")
        y = input("Segundo numero: ")
        res = int(x - y)
        print x, "-", y, "=", res
 
    elif opcion == 3:
        print "Multiplicacion"
        x = input("Primer numero: ")
        y = input("Segundo numero: ")
        mul = int(x * y)
        print x, "*", y, "=", mul
        break
 
    elif opcion == 4:
        print "Division"
        x = input("Primer numero: ")
        y = input("Segundo numero: ")
        div = int(x / y)
        print x, "/", y, "=", div
 
else:
        print "No es opcion Valida"
 
#print "AQuieres otra operacion"