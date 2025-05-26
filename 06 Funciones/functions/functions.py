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

