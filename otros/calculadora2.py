#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 23:30:33 2017

@author: tizianomartinhernando
"""

def hanoi(N, inc='1', temp='2', fin='3'):

    if N > 0:

        hanoi(N - 1, inc, fin, temp)

        print('se mueve de torre', inc, 'a torre', fin)

        hanoi(N - 1, temp, inc, fin)

discos = int(input("Introducir el numero de discos:"))

hanoi(discos)
