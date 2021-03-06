#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 23:46:48 2017

@author: tizianomartinhernando
"""

# Primer programa de caída libre
# Una pelota se deja caer desde x0=1 m
# Desde una altura de 50 m
# Se observa en un tiempo [0,tn)
# edelros@espol.edu.ec

import numpy as np
import matplotlib.pyplot as plt

# Ingreso de variables
tn=int(input('Cuantos segundos:'))
x=np.zeros(tn,dtype=float)
y=np.zeros(tn,dtype=float)
t=np.zeros(tn,dtype=float)

# condiciones iniciales
t[0]=0
x[0]=1
y[0]=50

# calcular los otros puntos
i=1
while (i<tn):
    t[i]=t[i-1]+1
    x[i]=x[0]
    y[i]=y[0]+0*t[i]+0.5*(-9.8)*(t[i]**2)
    i=i+1

#salida
plt.scatter(x,y)
plt.show()