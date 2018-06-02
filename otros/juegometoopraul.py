#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:40:50 2017

@author: tizianomartinhernando
"""

import random

print (" --- MASTERMIND --- \n")
print ("Adivina el cÃ³digo secreto de colores en el menor nÃºmero de veces.\n")
print ("Por favor, introduce tu cÃ³digo de colores.\nPuedes usar rojo(R), verde(V), azul(Z), amarillo(A), blanco(B) y rosa(S)")

colors = ["R", "V", "Z", "A", "B", "S"]
attempts = 0
game = True

# computer randomly picks four-color code
color_code = random.sample(colors,4)	
print (color_code)

# player guesses the number	
while game:
    correct_color = ""
    guessed_color = ""
    player_guess = input().upper()
    attempts += 1
	
    # checking if player's input is correct
    if len(player_guess) != len(color_code):
        print ("\nEl cÃ³digo secreto tiene, exÃ¡ctamente, cuatro colores. Venga, sÃ© que puedes contar hasta cuatro. Â¡IntÃ©ntalo otra vez!")
        continue
    for i in range(4):
        if player_guess[i] not in colors:
            print ("\nRevisa quÃ© colores puedes utilizar. Â¿No serÃ¡s daltÃ³nico?")
            continue
			
    # comparison between player's input and secret code
    if correct_color != "XXXX":
        for i in range(4):
            if player_guess[i] == color_code[i]:
                correct_color += "X"
            if  player_guess[i] != color_code[i] and player_guess[i] in color_code:
                guessed_color += "O"
        print (correct_color +  guessed_color + "\n")		
		
    if correct_color == "XXXX":
        if attempts == 1:
            print ("Â¡Guau! Â¡Al primer intento! Eres un fenÃ³meno")
        else:
            print ("Bien hecho... has necesitado " + str(attempts) + " intentos.")
        game = False
		
    if attempts >= 1 and attempts <6 and correct_color != "XXXX":
        print ("Siguiente intento: ")
    elif attempts >= 6:
        print ("Â¡No lo has adivinado! El cÃ³digo secreto de colores era: " + str(color_code))
        game = False

    # play or not to play
    while game == False:
        finish_game = input("\nÂ¿Quieres jugar otra (S/N)? ").upper()	
        attempts = 0
        if finish_game =="N":
            print ("\nÂ¡Gracias! Bye, bye.")
            game = None
        elif finish_game == "S":
            game = True
            print ("\nÂ¡Jueguemos una vez mÃ¡s! Adivina el cÃ³digo secreto: ")

# --- end --- #