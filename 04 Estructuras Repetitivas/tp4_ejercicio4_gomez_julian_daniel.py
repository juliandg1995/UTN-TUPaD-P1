# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# := Es un operador de asignación en expresión. 
# Permite asignar un valor a una variable y al mismo tiempo evaluar la expresión. Esto es útil para evitar escribir código redundante
# Tener en cuenta que se deben ingresar paréntesis para que la asignación se realice antes de la evaluación de la condición.

suma = 0
while (numero := int(input("Ingrese un número entero (0 para salir): "))) != 0:
    suma += numero

print(f"La suma total es: {suma}")