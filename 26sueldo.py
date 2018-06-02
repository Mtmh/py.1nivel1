#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 23:48:09 2017

@author: tizianomartinhernando
"""
sueldo=int(input('ingrese sueldo de empleado: '))
antiguedad=int(input('Ingrese su antiguedad en años: '))
if sueldo<500 and antiguedad>10:
    aumento=sueldo*0.20
    sueldototal=sueldo+aumento
    print('Sueldo a pagar: ')
    print(sueldototal)
else:
    if sueldo<500:
        aumento=sueldo*0.05
        sueldototal=sueldo+aumento
        print('Sueldo a pagar: ')
        print(sueldototal)
    else:
        print('Sueldo a pagar: ')
        print(sueldo)
        