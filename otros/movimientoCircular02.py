#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:19:33 2017

@author: tizianomartinhernando
"""

# FCNM-ESPOL-2015. Fisica con Python
# Una particula en recorrido circular
# Con trayectoria y vector velocidad
# propuesta: edelros@espol.edu.ec

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# inicializa parametros de fotos
fotos=100
figura, cuadro = plt.subplots()
plt.axis('equal')
plt.axis([-2, 2, -2, 2])

# Valores iniciales de la grafica (1er frame)
# posicion del punto
angulo=0
x = np.cos(angulo)      # x-escalar
y = np.sin(angulo)      # y-escalar
# velocidades en el punto
vx= -np.sin(angulo)
vy= np.cos(angulo)

# dibuja el punto y velocidades
punto, = cuadro.plot(x,y,'ro')
velocidad, = cuadro.plot([x,x+vx],[y,y+vy],'*-')
velx, =cuadro.plot([x,x+vx],[y,y],'*-.')
vely, =cuadro.plot([x,x],[y,y+vy],'*-.')
# Dibuja trayectoria circular
alfa= np.linspace(0,2*np.pi,fotos)
xt= np.cos(alfa)
yt= np.sin(alfa)
trayecto = cuadro.plot(xt,yt)

# Empieza la Animación
# Nuevas gráficas
def redibuja(t):
    # determina los puntos x,y para cada t
    angulo=(2*np.pi/fotos)*t
    x=np.cos(angulo)
    y=np.sin(angulo)
    # velocidad del punto
    vx= -np.sin(angulo)
    vy= np.cos(angulo)
    
    # actualiza gráficas
    punto.set_xdata(x) # actualiza el punto
    punto.set_ydata(y)
    velocidad.set_xdata([x,x+vx])
    velocidad.set_ydata([y,y+vy])
    velx.set_xdata([x,x+vx])
    velx.set_ydata([y,y])
    vely.set_xdata([x,x])
    vely.set_ydata([y,y+vy])
    return punto, velocidad, velx, vely,

# Init se requiere para limpiar la pizarra
def borrapizarra():
    punto.set_ydata(np.ma.array(x, mask=True))
    velocidad.set_ydata(np.ma.array(x, mask=True))
    velx.set_ydata(np.ma.array(x, mask=True))
    vely.set_ydata(np.ma.array(x, mask=True))
    return punto, velocidad, velx, vely,

# contador de fotos
t = np.arange(1, fotos)
ani = animation.FuncAnimation(figura, redibuja, t , init_func=borrapizarra,
    interval=10, blit=True)
plt.show()