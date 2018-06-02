#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 23:44:54 2017

@author: tizianomartinhernando
"""

# FCNM-ESPOL-2015. Fisica con Python
# Una particula en recorrido circular
# propuesta: edelros@espol.edu.ec

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Inicializa parametros de graficas (frames)
fotos=100
figura, cuadro = plt.subplots()
plt.axis('equal')
plt.axis([-1.5, 1.5, -1.5, 1.5])
# Valores iniciales de la grafica (1er frame)
angulo=0
x = np.cos(angulo)        # x-escalar
y = np.sin(angulo)        # y-escalar

punto, = cuadro.plot(x, y,'ro')

# Empieza la Animación
# Nuevas gráficas (n frame)
def redibuja(t):
    # determina los puntos x,y para cada t
    angulo=(2*np.pi/fotos)*t
    x=np.cos(angulo)
    y=np.sin(angulo)
    
    punto.set_xdata(x) # actualiza el punto
    punto.set_ydata(y)  
    return punto,

# Requerido para limpiar gráfica
def borrapizarra():
    punto.set_ydata(np.ma.array(x, mask=True))
    return punto,

# Genera nuevas gráficas
t = np.arange(1, fotos)
ani = animation.FuncAnimation(figura, redibuja, t , init_func=borrapizarra,
    interval=10, blit=True)
plt.show()