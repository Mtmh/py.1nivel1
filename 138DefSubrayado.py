#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 00:30:50 2017

@author: tizianomartinhernando
"""

def titulo_subrayado(titulo,caracter="*"):
    print(titulo)
    print(caracter*len(titulo))


# bloque principal

titulo_subrayado("Sistema de Administracion")
titulo_subrayado("Ventas","-")

'''
Confeccionar una función que reciba un string como parámetro
 y en forma opcional un segundo string con un caracter.
 La función debe mostrar el string subrayado
 con el caracter que indica el segundo parámetro'''
 