#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:10:13 2017

@author: tizianomartinhernando
"""

'''
Desarrollar una clase llamada Lista, que permita pasar al
 método __init__ una lista de valores enteros.
 
Redefinir los operadores +,-,* y // con respecto a un valor
 entero.'''
 
class Lista:
    
    
    def __init__(self,lista):
        self.lista=lista
    
    
    def imprimir(self):
        print(self.lista)
        
    def __add__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]+entero)
        return nueva
    
    def __sub__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]-entero)
        return nueva
    
    def __mul__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]*entero)
        return nueva
    
    def __floordiv__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]/entero)
        return nueva

# bloque principal
        
lista1=Lista([3,4,5])
lista1.imprimir()
print(lista1+10)
print(lista1-10)
print(lista1*10)
print(lista1//10)

    
