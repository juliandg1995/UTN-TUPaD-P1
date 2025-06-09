import time, random

# Función para leer un número entero positivo
def leer_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(f"{mensaje}"))
            if numero < 0:
                print("Por favor, ingrese un número entero positivo.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

# Función que genera una lista de números aleatorios en el rango de 1 a n*2
def generar_lista_aleatoria_A(tamanio):
    return random.sample(range(1, tamanio * 2 + 1), tamanio)

# Función que genera una lista de números aleatorios en el rango de 1 a n
def generar_lista_aleatoria_B(tamanio):
    return random.sample(range(1, tamanio + 1), tamanio)


# Algoritmo de búsqueda lineal mediante estructura iterativa secuencial
def busqueda_lineal(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1

# Algoritmo de búsqueda binaria mediante estructura iterativa
# Requiere que la lista esté ordenada para que no falle
def busqueda_binaria(lista, objetivo):
    izquierda = 0                       # Índice inicial de la búsqueda (primer elemento)
    derecha = len(lista) - 1            # Índice final de la búsqueda (último elemento)
    while izquierda <= derecha:          # Mientras el rango de búsqueda sea válido
        medio = (izquierda + derecha) // 2   # Calcula el índice medio (redondeado hacia abajo)
        if lista[medio] == objetivo:         # Si el elemento del medio es el objetivo
            return medio                     # Retorna la posición donde se encontró
        elif lista[medio] < objetivo:        # Si el elemento del medio es menor al objetivo
            izquierda = medio + 1            # Busca en la mitad derecha (descarta la izquierda)
        else:                                # Si el elemento del medio es mayor al objetivo
            derecha = medio - 1              # Busca en la mitad izquierda (descarta la derecha)
    return -1                                # Si no se encuentra, retorna -1

def medir_tiempo(funcion, *args):
    inicio = time.perf_counter()
    resultado = funcion(*args)
    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000
    return resultado, tiempo_ms