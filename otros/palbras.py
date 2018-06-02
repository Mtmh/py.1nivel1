#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 16:00:00 2017

@author: tizianomartinhernando
"""

def test():
    print('Deteccion de palabras con la expresion "ta"')
    print('Version 1: cargando los caracteres uno a uno...')
cl = 0
ctp = 0
cpp = 0
cta = 0
st = False
sta = False
print('Ingrese las letras del texto, pulsalso <Enter> una a una')
print('(Para finalizar la carga, ingrese un punto)')
print()
car = None
while car != '.':
    car = input('Letra  (con punto termina): ')
    cl += 1
    
    if car == ' ' or car == '.':
        if cl > 1:
            ctp += 1
        if sta:
            cta += 1
        cl = 0
        st = sta = False
        continue
    if cl == 1 and car == 'p':
        cpp += 1
    if car == 't':
        st = True
    else:
        if car == 'a' and st:
            sta = True
        st = False
print('1. Cantidad total de palabras:', ctp)
print('2. Cantidad de palabras que empiezan con "p":', cpp)
print('3. Cantidad de palabras con la expresion "ta!:', cta)

    
    
    