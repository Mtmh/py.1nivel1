# --- MASTERMIND --- #

#importar módulo ramdom
import random

print (" --- MASTERMIND --- \n")
print ("Adivina el código secreto de colores en el menor número de veces.\n")
print ("Por favor, introduce tu código de colores.\nPuedes usar rojo(R), verde(V), azul(Z), amarillo(A), blanco(B) y rosa(S)")

colores = ["R", "V", "Z", "A", "B", "S"]
intentos = 0
jugar = True
daltonico = False

# el ordenador elige un código de cuatro coleres aleatoriamente
codigo_colores = random.sample(colores,4)	
''' # En el primer juego me revela el código para aprender
Comentar la siguiente línea para no revelarlo # ''' 
print (codigo_colores)

# el jugador adivina el código	
while jugar:
    color_correcto = ""
    color_adivinado = ""
    jugador_adivina = input("¿Tu código? ").upper()
    intentos += 1
	
    # verificar que la entrada del jugador es correcta
    if len(jugador_adivina) != len(codigo_colores):
        print ("\nEl código secreto tiene, exáctamente, cuatro colores.")
        print ("Venga, sé que puedes contar hasta cuatro.")
        print ("¡Inténtalo otra vez!")
        #'continue' despues de un 'while' 
        #vuelve al inicio de 'while'
        continue
    for i in range(4):
        if jugador_adivina[i] not in colores:
            daltonico = True
            #'continue' despues de un 'for'
            #termina el 'for' pero continua con el resto
            continue
    if daltonico == True:
        print ("\n¿No serás daltónico?")
        print ("Puedes usar rojo(R), verde(V), azul(Z), amarillo(A), blanco(B) y rosa(S)")
        daltonico = False
			
    # comparar la entrada del jugador y el código secreto
    if color_correcto != "XXXX":
        for i in range(4):
            if jugador_adivina[i] == codigo_colores[i]:
		#el color está en la posición adecuada
                color_correcto += "X"
            if  jugador_adivina[i] != codigo_colores[i] and jugador_adivina[i] in codigo_colores:
		#el color está pero no en la posición adecuada
                color_adivinado += "O"
        print (" " + color_correcto +  color_adivinado + "\n")		
		
    if color_correcto == "XXXX":
        if intentos == 1:
            print ("¡Guau! ¡Al primer intento! Eres un fenómeno")
        else:
            print ("Bien hecho... has necesitado " + str(intentos) + " intentos.")
        jugar = False
		
    if intentos >= 1 and intentos <6 and color_correcto != "XXXX":
        print ("Siguiente intento: ")
    elif intentos >= 6:
        print ("¡No lo has adivinado! El código secreto de colores era: " + str(codigo_colores))
        jugar = False

    # play or not to play
    while jugar == False:
        terminar_juego = input("\n¿Quieres jugar otra (S/N)? ").upper()	
        intentos = 0
        if terminar_juego =="N":
            print ("\n¡Gracias! Bye, bye.\n")
            jugar = None
        elif terminar_juego == "S":
            jugar = True
            print ("\n¡Jueguemos una vez más! Adivina el código secreto: ")
codigo_colores = random.sample(colores,4)	            

# --- fin --- #
