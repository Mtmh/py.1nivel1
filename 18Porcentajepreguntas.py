#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 22:20:04 2017

@author: tizianomartinhernando
"""
total_preguntas = int(input('Ingrese la cantidad total de preguntas del examen: '))
total_correctas = int(input('Ingrese cantidad total de preguntas contestadas correctamente: '))
porcentaje = total_correctas * 100 / total_preguntas
if porcentaje >= 90:
    print('Nivel maximo')
else:
    if porcentaje >= 75:
        print("Nivel medio")
    else:
        if porcentaje >= 50:
            print('Nivel regular')
        else:
            print('Fuera de nivel')
            
    
    

