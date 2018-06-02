#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:58:27 2017

@author: tizianomartinhernando
"""
num = int(input('Ingrese un valor positivo de tres cifras: '))
if num < 10:
    print('Tiene un digito')
     
else:
    if num < 100:
        print('Tiene dos digitos')
    else:
        if num < 1000:
            print('Tiene tres digitos')
        else:
            print('Error en la entrada de datos.')
            
                
                
                
            
                
            
