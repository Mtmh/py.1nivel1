#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 17:05:18 2017

@author: tizianomartinhernando
"""

def cantidad_vocal_a(palabra):
    cant=0
    for x in range(len(palabra)):
        if palabra[x]=='a' or palabra[x]=="A":
            cant=cant+1
    return cant


# bloque principal

palabra=input("Ingrese una palabra:")
print("La palabra",palabra,"tiene",cantidad_vocal_a(palabra),"a")