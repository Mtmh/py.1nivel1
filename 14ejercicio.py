#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:09:24 2017

@author: tizianomartinhernando
"""

nota1 = int(input('Ingrese primera nota: '))
nota2 = int(input('Ingrese segunda nota: '))
nota3 = int(input('Ingrese tercera nota: '))
prom = (nota1+nota2+nota3)/3

if prom >= 7:
    print('Promocionado')
else:
    if prom >= 4:
        print('Regular')
    else:
        print('Reprobrado')
        
