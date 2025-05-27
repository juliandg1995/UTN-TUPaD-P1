# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun-
# ción

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions')))
import functions as funciones

# Imprime una tabla de multiplicar de un número entero dado:
funciones.tabla_multiplicar(funciones.ingresar_numero_entero("Ingrese un número entero para ver su tabla de multiplicar: ", 1, 100))