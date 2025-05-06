# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
contador = 0

while numero != 0:
    numero = numero // 10
    contador += 1
print("La cantidad de dígitos es:", contador)