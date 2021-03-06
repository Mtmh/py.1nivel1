raul# Importamos módulos

from random import randint
import time

# Declaramos variables
segundo=int(time.strftime("%S"))
# Para ejecutar en el IDE Spyder es necesario
# inicializar las siguientes a cero(0)

bot=0
jug=0

#El juego empieza aquí
jugador=input("¿Tu nombre? Me gusta saber con quien juego: ")
print("Bien, ", jugador,", preparate", sep='')
partidas=int(input("Cuantas partidas quieres que juguemos?: ")) 

#Llamamos a las funciones tantas veces como se haya almacenado en [partida] 
for x in range(0,partidas):
    print("\nPartida ", x+1, "de ", partidas)
    
    #jugada = jugada_usuario()
    jugada = 0 
    while jugada < 1 or jugada > 3: 
        jugada = int(input("Selecciona: piedra(1) / papel(2) / tijera (3): ")) 
        if jugada == 1: 
            print (jugador, ": piedra") 
        elif jugada == 2: 
            print (jugador, ": papel") 
        elif jugada == 3: 
            print (jugador, ": tijera") 
        else: 
            print ("Introduce un número entre 1 y 3")
    
    #bot_jug = jugada_bot()
    bot_jug = randint(1, 3) 
    if bot_jug == 1: 
        print ("máquina: piedra")
    elif bot_jug == 2: 
        print ("máquina: papel")
    elif bot_jug == 3: 
        print ("máquina: tijera")

    #ganador(jugada,bot_jug)
    if jugada == bot_jug: 
        print ("\n", "Empate", "\n") 
    elif jugada == 1 and bot_jug == 2 or jugada == 3 and bot_jug == 1 or jugada == 2 and bot_jug == 3: 
        print ("\n", "La máquina gana", "\n")
        bot+=1
    else: 
        print ("\n", "Tu ganas", "\n")
        jug+=1 

'''Mostramos el resultado en función de los valores en [bot] y [jug]
que ha ido acumulando la función ganador()'''
if bot > jug:
    print("Te he ganado",bot,jug)
elif  jug > bot:
    print("Me has ganado",jug,bot)
else:
    print("Parece que hemos empatado",jug,bot)
