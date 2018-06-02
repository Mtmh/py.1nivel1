#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:15:33 2017

@author: tizianomartinhernando
"""

print('Ingrese tres numeros diferentes')
num1 = int(input('Primer numero: '))
num2 = int(input('Segundo numero: '))
num3 = int(input('Tercer numero: '))
if num1 > num2:
    print(num1)
else:
    if num2 > num3:
        print(num2)

    elif num3 > num2:
        print(num3)
    
        


