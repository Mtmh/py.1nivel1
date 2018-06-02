#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:28:45 2017

@author: tizianomartinhernando
"""

'''
5)
Lo mismo que el anterior pero ordenando de mayor a menor.'''

lista=[]
salir=False

while(not salir):
    
    numero=int(input('Dame un numero: '))
    
    if(numero==0):
        salir=True
    else:
        lista.append(numero)
lista.sort(reverse=True)# ordena la lista
print(lista)
