#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 18:45:24 2017

@author: tizianomartinhernando
"""

'''
Implementar una clase llamada Alumno que tenga como atributos
 su nombre y su nota. Definir los métodos para inicializar
 sus atributos, imprimirlos y mostrar un mensaje si está regular
 (nota mayor o igual a 4)
Definir dos objetos de la clase Alumno.'''

class Alumno:
    
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        
    def imprimir(self):
        print('Nombre: ',self.nombre)
        print('Nota: ',self.nota)
    
    def mostrar_estado(self):
        if self.nota>=4:
            print('Regular')
        else:
            print('Libre')

# bloque principal
            
alumno1=Alumno()
alumno1.inicializar('diego',2)
alumno1.imprimir()
alumno1.mostrar_estado()


alumno2=Alumno()
alumno2.inicializar('ana',10)
alumno2.imprimir()
alumno2.mostrar_estado()

