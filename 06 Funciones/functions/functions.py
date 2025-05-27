import math

#----------- COMIENZO FUNCIONES AUXILIARES -----------###

# Función que se usa para ingresar un número flotante
def ingresar_numero_flotante(mensaje, minimo=float("-Inf"), maximo=float("Inf")):    
    while True:
        try:
            num = float(input(mensaje))
            if minimo <= num <= maximo:
               return num
            else:
                print(f"\nPor favor, ingrese un número dentro del rango [{minimo},{maximo}]") 
        except ValueError:
            print("\nPor favor, ingrese un número válido.")

# Función que se usa para ingresar un número entero
def ingresar_numero_entero(mensaje, minimo=float("-Inf"), maximo=float("Inf")):    
    while True:
        try:
            num = int(input(mensaje))
            if minimo <= num <= maximo:
               return num
            else:
                print(f"\nPor favor, ingrese un número dentro del rango [{minimo},{maximo}]") 
        except ValueError:
            print("\nPor favor, ingrese un número válido.")

#----------- FIN FUNCIONES AUXILIARES -----------###

# Saludo: Hola, Mundo!
def imprimir_hola_mundo():
    print("Hola, Mundo!")

# Saludo: Hola, {nombre}!
def saludo_usuario(nombre):
    print(f"Hola, {nombre}!")

# Imprime Información Personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"""\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.\n""")

# Calcula el area de un círculo dado su radio
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

# Calcula el perímetro de un círculo dado su radio
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Convierte de segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# Imprime la tabla de multiplicar de un número dado
def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()
    
# Devuelve operaciones básicas entre dos números:
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = None if b == 0 else a / b  # Evita división por cero

    return (f"{a} + {b} = {suma}", 
            f"{a} - {b} = {resta}", 
            f"{a} * {b} = {multiplicacion}", 
            f"{a} / {b} = {division}")

# Calcula el índice de masa corporal (IMC)
def calcular_imc(peso, altura):
    if altura <= 0:
        return None  # Se evita división por cero o altura negativa
    imc = peso / (altura ** 2)
    return round(imc, 2)

# Calcula de celcius a fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Calcula el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3