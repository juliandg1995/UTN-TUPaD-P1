# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions')))
import functions as funciones

celcius = funciones.ingresar_numero_flotante("Ingrese la temperatura en grados Celsius: ")
print(f"\n La temperatura de {celcius}°C convertida a Farenheit es: {funciones.celsius_a_fahrenheit(celcius)}°F\n")