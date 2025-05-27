# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions')))
import functions as funciones

a = funciones.ingresar_numero_flotante("Ingrese el primer número: ")
b = funciones.ingresar_numero_flotante("Ingrese el segundo número: ")
c = funciones.ingresar_numero_flotante("Ingrese el tercer número: ")

print(f"\nEl promedio de los números {a}, {b} y {c} es: {funciones.calcular_promedio(a, b, c)}\n")
