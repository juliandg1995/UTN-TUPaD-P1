import math

### Ingresar nro entero positivo ####
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
            
            
### Calcular factorial de un número con recursividad ####
def factorial(n):
    if n < 0:
        return None  # Factorial no está definido para números negativos
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

### Calcula el valor de la posición indicada dentro de Fibonacci ###
def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci de forma recursiva."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
### Cálculo de potencia recursiva ###
def potencia(base, exponente):
    if (exponente == 0):
        return 1
    else:
        return base * potencia(base, exponente - 1)