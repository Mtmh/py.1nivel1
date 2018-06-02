#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 23:50:57 2017

@author: tizianomartinhernando
"""

import random
monedas = int(input("Cuantas monedas tiene?: "))
#Procedimiento
caja=15
trio=0
par=0
turno=0
while (monedas>=5 and caja>=15):
 turno=turno+1
 monedas=monedas-5
 caja=caja+5
 a=int(random.random()*10)
 b=int(random.random()*10)
 c=int(random.random()*10)
 if (a==b and b==c and c==a):
     caja = caja-20
     monedas=monedas+20
     trio=trio+1
else:
  if (a==b or b==c or c==a):
      caja=caja-10
      monedas=monedas+10
      par=par+1
#Salida
print(" Se jugaron " + str (turno) + " turnos.")
print(" Trios: "+str(trio))
print(" Pares: "+str(par))
print(" monedas jugador: "+str(monedas))
  
