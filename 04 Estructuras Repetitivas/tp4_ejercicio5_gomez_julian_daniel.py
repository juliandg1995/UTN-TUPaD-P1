# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

stop = ''
intentos = 1
acertado = random.randint(0,10)

# El juego da pistas al usuario sobre si el número ingresado es mayor o menor al número correcto.
while ( (numero := int(input("Ingrese un número entero entre el 0 y el 10: "))) != acertado and stop != 'X'):
    if numero < acertado:
        print("El número ingresado es menor al buscado.\n")
    else:
        print("El número ingresado es mayor al buscado.\n")
    intentos += 1
    stop = input("¿Desea continuar? (X para salir): ").upper()
    
if numero == acertado:    
    print(f"\n¡Felicitaciones! Adivinaste el número {acertado} en {intentos} intentos.")
else:
    print(f"\nEl número era {acertado}. Saliste después de {intentos} intentos.")