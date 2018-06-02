#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 18:34:37 2017

@author: tizianomartinhernando
"""

'''
Implementaremos una clase llamada Persona
 que tendrá como atributo (variable) su nombre y dos métodos
 (funciones), uno de dichos métodos inicializará el atributo
 nombre y el siguiente método mostrará en la pantalla
 el contenido del mismo.'''
 

class Persona:
    def inicializar(self,nom):
        self.nombre=nom
        
    def imprimir(self):
        print('Nombre',self.nombre)

# bloque principal
        

persona1=Persona()
persona1.inicializar('Pedro')
persona1.imprimir()

persona2=Persona()
persona2.inicializar('Carla')
persona2.imprimir()

'''
Como veremos todo método tiene como primer parámetro
 el identificador 'self'que tiene la referencia del 
 objeto que llamó al método'''