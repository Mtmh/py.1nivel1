#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:45:36 2017

@author: tizianomartinhernando
"""

'''
Crea una tupla con números,
 pide un numero por teclado e indica cuantas veces se repite'''
 
'''numeros=(5,4,3,2,1,6,45,3,6,6,6,6,6)
numero=int(input('Dame un numero: '))
 
contador=0
for i in numeros:
    if numero==1:
        contador=contador+1
print('Hay',contador,'repiticiones/es')'''


numeros = (7,6,5,4,3,2,3,4,5,1,4,3)
 
numero = int(input("Dame un numero: "))
 
print("Numero de repeticiones: ",numeros.count(numero))

