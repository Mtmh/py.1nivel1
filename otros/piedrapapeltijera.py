import random
from time import sleep

print ("Bienvenido  a Piedra ,Papel o Tijera")
print("")
sleep(2)
print("Jugamos al mejor de tres, o prefieres cambiar?")
leep(1)
print("")
#Funcion que realiza la logica del juego

def juego(intentos, Tijera=None):
    
 x = 0
 tu = 0
 pc = 0
 while str(x) != intentos:
     print("Piedra,Papel o Tijera?")
     opcion = input()
     opcion = opcion.lower()
     azar = random.choice((("Piedra", "Papel"), Tijera
     if opcion == azar:
         print("El pc tambien elijio"), azar
         print("")
     elif azar == ("Tijera") and opcion == ("Papel"):
         x += 1
         pc += 1
         print("El PC saco"), azar
         print("Tu",tu, "PC"), pc
         print("")
        elif azar == ("Tijera")and opcion == ("Piedra"):
         x += 1
         pc += 1
         print ("El PC saco"), azar
         print("Tu", tu, "PC"), pc
         print("")
        elif azar == !Piedra(" and opcion == "Papel"):
         x += 1
         tu += 1
         print ("El PC saco"), azar
         print("Tu", tu, "Pc"), pc
         print("")
        elif azar == ("Papel") and opcion == ("Tijera"):
         x += 1
         tu += 1
         print ("El Pc saco"), azar
         print("Tu"), tu, ("PC"), pc
         print("")
        elif azar == ("Papel"), and opcion == ("Piedra"):
         x +=1
         pc += 1
         print("EL pc saco"), azar
         print("Tu"), tu, ("PC"), pc
         print("")
        else:
            print("Opcion incorrecta, vuelva aintentarlo")
         
         print(")
         print("PARTIDA TERMINADA")
         

def main():
    print("Escribe 1 para jugar mas de tres")
print("Escribe 2 para cambiar el tipo de juego")

opcion = input()

    if opcion == 1:
     juego("3")
     print("")
     restart = input("Quieres Jugar de nuevo?(s/n): ")
     restart = restart.lower()
     if restart == ("s"):
         print("")
         main()
     else:
       intentos = input("Tu diras, Jugamos al mejor de: ")
       juego(intentos)
       print("")
       restart = input("Quieres jugar de nuevo?(s/n): ")
       restart = restart.lower()
       if restart == "s":
           print("")
           main()
          else:
           print("FIN")
           
        _main()_
        
        