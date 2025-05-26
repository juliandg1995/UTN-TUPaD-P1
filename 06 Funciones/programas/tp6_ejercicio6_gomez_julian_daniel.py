# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos-
# trar el resultado usando esta función

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions')))
import functions as funciones

# Imprime una tabla de multiplicar de un número entero dado:
funciones.tabla_multiplicar(funciones.ingresar_numero_entero("Ingrese un número entero para ver su tabla de multiplicar: ", 1, 100))