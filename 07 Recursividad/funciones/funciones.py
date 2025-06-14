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
    
    
### Convertir de decimal a binario
def decimal_a_binario(decimal):
    # 2 casos base: O la división resulta en 1 o en 0 
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    else:
        #La cadena binaria se arma dinámicamente, sin necesidad de declararla dentro de la fn
        return decimal_a_binario(decimal // 2) + str(decimal % 2)
    

# Determina si la palabra es palindromo de manera recursiva
# Verifica si los extremos de la cadena son iguales y los elimina hasta vaciar la cadena
def es_palindromo(palabra):
    if (len(palabra) <= 1):
        return True
    if (palabra[0] != palabra[-1]):
        return False
    return es_palindromo(palabra[1:-1])  # Llamada recursiva con la palabra sin los extremos


# Suma todos los dígitos de un número
def suma_digitos(n):
    if n == 0:
        return 0
    return suma_digitos(n//10) + n % 10

# Sumo todos los bloques de una pirámide con base n
# Utilizo una sumatoria recursiva quitando 1 bloque por nivel
def contar_bloques(n):
    if n == 0:
        return 0
    return contar_bloques(n-1) + sum(range(1,n+1))
 
    
# Cuenta cuántas veces aparece un dígito en un número entero positivo
def contar_digito(numero,digito):
    """Cuenta cuántas veces aparece un dígito en un número entero positivo."""
    if numero == 0:
        return 0
    else:
        return contar_digito(numero // 10, digito) + ( 1 if numero % 10 == digito else 0 ) 