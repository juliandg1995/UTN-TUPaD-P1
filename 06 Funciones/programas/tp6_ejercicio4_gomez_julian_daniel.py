# Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
# dio como parámetro y devuelva el área del círculo. calcular_peri-
# metro_circulo(radio) que reciba el radio como parámetro y devuel-
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
# bas funciones para mostrar los resultados

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions')))
import functions as funciones

radio = funciones.ingresar_numero_flotante("Ingrese el radio de un círculo: ")
print(f"\nEl área del círculo es: {funciones.calcular_area_circulo(radio):.2f}")
print(f"\nEl perímetro del círculo es: {funciones.calcular_area_circulo(radio):.2f}")
