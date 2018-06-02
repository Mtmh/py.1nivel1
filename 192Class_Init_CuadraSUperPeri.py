#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:06:12 2017

@author: tizianomartinhernando
"""

'''
Desarrollar una clase que represente un Cuadrado y tenga
 los siguientes métodos:
  inicializar el valor del lado llegando como parámetro
  al método __init__ (definir un atributo llamado lado)
  , imprimir su perímetro y su superficie. '''
  
class Cuadrado:
    
    def __init__(self,lado):
        self.lado=lado
        
    def mostrar_perimetro(self):
        per=self.lado*4
        print('El perimetro de cuadrado es: ',per)
        
    
    def mostrar_superficie(self):
        sup=self.lado*self.lado
        print('La superficie del cuadrado es: ',sup)
        
# bloque principal
        

cuadrado1=Cuadrado(12)
cuadrado1.mostrar_perimetro()
cuadrado1.mostrar_superficie()
