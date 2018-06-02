entero=input('Introduzca un numero entero: ')

try:
    entero=int(entero)
    print("Enhorabuena has ingresado un numero entero: ", entero)
except ValueError:
    print("Error no has ingresado un numero entero ")

'''Son excepciones para los despistados'''