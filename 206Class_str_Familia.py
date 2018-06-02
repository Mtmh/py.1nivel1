#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 18:38:50 2017

@author: tizianomartinhernando
"""

'''
Declarar una clase llamada Familia.
 Definir como atributos el nombre del padre, madre y una lista
 con los nombres de los hijos.
 
Definir el método especial __str__ que retorne un string
 con el nombre del padre, la madre y de todos sus hijos.'''
 
class Familia:

    def __init__(self,padre,madre,hijos=[]):
        self.padre=padre
        self.madre=madre
        self.hijos=hijos

    def __str__(self):
        cadena=self.padre+","+self.madre
        for hi in self.hijos:
            cadena=cadena+","+hi
        return cadena


# bloque principal

familia1=Familia("Pablo","Ana",["Pepe","Julio"])
familia2=Familia("Jorge","Carla")
familia3=Familia("Luis","Maria",["marcos"])

print(familia1)
print(familia2)
print(familia3)
