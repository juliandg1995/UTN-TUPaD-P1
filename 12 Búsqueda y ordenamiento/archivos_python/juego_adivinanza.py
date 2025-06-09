import funciones as fn
import random

# Juego de adivinanza de números con búsqueda lineal y binaria

# Se pide al usuario el tamaño de la lista
tamanio = fn.leer_entero_positivo("Ingrese el tamaño de la lista (número entero positivo): ")

print(f"\nIngrese:\n - A si desea que la lista tenga números aleatorios dentro del rango de 1 a {tamanio} * 2, o \n - B si desea que la lista tenga números secuenciales dentro del rango de 1 a {tamanio} \n")

opcion = input("Ingrese A o B: ").upper()
# Se valida la opción ingresada
while opcion not in ['A', 'B']:
    print("Opción inválida. Por favor, ingrese A o B.")
    opcion = input("Ingrese A o B: ").upper()
 
if opcion == 'A':
    # Se genera una lista de números dentro de un rango 1 a n*2
    print("Se generará una lista de números aleatorios dentro del rango de 1 a n*2.")
    lista = fn.generar_lista_aleatoria_A(tamanio)   
else:
    print("Se generará una lista de números secuenciales dentro del rango de 1 a n.")
    lista = fn.generar_lista_aleatoria_B(tamanio)
    
# Se ordenar la lista
lista.sort()
# Se elige un número secreto a adivinar
numero_secreto = random.choice(lista)

print(f"\nLista:\n{lista}\n")

#####    A continuación, se busca la posición del número secreto    #####
#   Se utilizan parámetros genéricos (*args) en la función medir_tiempo para poder medir el 
# tiempo de ejecución de distintas funciones
#   Como medir_tiempo retorna una tupla con el índice encontrado y el tiempo, 
# se descompone su resultado en dos variables separadas por coma
pos, tiempo_blineal = fn.medir_tiempo(fn.busqueda_lineal, lista, numero_secreto)
pos, tiempo_bbinaria = fn.medir_tiempo(fn.busqueda_binaria, lista, numero_secreto)

# Se ejecutan tantos intentos de adivinanza como el usuario quiera hasta encontrar el número o decida salir
stop = ''
while stop.upper() != 'X':
    # Se pide el número al usuario
    numero_usuario = fn.leer_entero_positivo("Adivine el número secreto (ingrese un número entero): ")
    
    if numero_usuario not in lista:
        print("\nEl número ingresado no está en la lista. Intente de nuevo.")
        continue

    # Se informa si coincide con el número secreto o no
    if numero_usuario == numero_secreto:
        print("\n¡Felicitaciones! Ha adivinado el número secreto.\n")
        print(f"Número secreto: {numero_secreto}")
        print(f"Posición: {pos + 1}\n")
        print(f"Tiempo de búsqueda binaria: {tiempo_bbinaria:.3f} ms")
        print(f"Tiempo de búsqueda lineal: {tiempo_blineal:.3f} ms\n")
        break
    else:
        # Se informa si el número secreto es mayor o menor
        if numero_usuario < numero_secreto:
            print("El número secreto es mayor que el ingresado.\n")
        else:
            print("El número secreto es menor que el ingresado.\n")
        stop = input("Presione 'X' para salir o cualquier otra tecla para intentar de nuevo: ")
        print()
        
        
print("\nGracias por jugar. ¡Hasta la próxima!")