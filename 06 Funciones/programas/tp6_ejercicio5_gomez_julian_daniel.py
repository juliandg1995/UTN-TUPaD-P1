# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos-
# trar el resultado usando esta función

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions')))
import functions as funciones

segundos = funciones.ingresar_numero_flotante("Ingrese una cantidad de segundos: ")
print(f"\nEl equivalente en horas a {segundos} segundos es de {funciones.segundos_a_horas(segundos):.2f} horas")

