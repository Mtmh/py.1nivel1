#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 00:41:38 2017

@author: tizianomartinhernando
"""
from tkinter import *
ventana = Tk()
ventana.title('Ventana tkinter')
widget = Label(Ventana, text='Hola Gui tkinter')
widget.pack(expand=YES, fill=BOTH)
ventana.mainloop()
def menu():
    print('Menu de opciones y Funciones generalizadas')
    op = 1
    while op != 4:
        print('1.) : ')
        print('2.) : ')
        print('3.) : ')
        print('4.) : ')
        op =int(input('Ingrese un el numero de opcion elegida: '))
        if op == 1:
            opcion1()
        elif op == 2:
            opcion2()
        elif op == 3:
            opcion3()
menu()






