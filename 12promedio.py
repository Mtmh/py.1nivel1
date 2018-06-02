#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 23:16:32 2017

@author: tizianomartinhernando
"""
print('--------------------------------------')
print('****** Promedio de Notas *************')
print('--------------------------------------')
nota1 = int(input('Ingrese la primera nota: '))
nota2 = int(input('Ingrese la segunda nota: '))
nota3 = int(input('Ingrese la tercera nota: '))
print('\n*************************************')
promedio = (nota1 + nota2 + nota3)/3
if promedio >= 7:
    print('\nPromocionado ¡¡¡')
else:
    if promedio < 7:
        print('\nNo promocionado')
        
        

    
