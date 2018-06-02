#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:32:55 2017

@author: tizianomartinhernando
"""

clave=input('Ingrese la clave que tenga entre 10 y 20 caracteres: ')
if len(clave)>=10 and len(clave)<=20:
    print('largo correcto')
else:
    print('Largo incorrecto')
  
'''
Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en caso contrario mostrar un mensaje de error

'''

