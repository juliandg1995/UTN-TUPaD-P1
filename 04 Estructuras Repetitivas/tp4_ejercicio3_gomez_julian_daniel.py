# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# Valido que las entradas sean valores numéricos y no sean iguales
# Si los números son iguales, vuelvo a pedir los números
while True:
    try:
        numero1 = int(input("Ingrese el primer número entero: "))
        numero2 = int(input("Ingrese el segundo número entero: "))
        if numero1 != numero2:
            break
        print("Los números deben ser diferentes. Intente nuevamente.")
    except ValueError:
        print("Por favor, ingrese solo números enteros.")

# Realizo la suma de los números enteros entre los dos valores dados (excluyendo los extremos)
# Utilizo min y max para asegurarme de que el rango sea correcto y no importe el orden de los números
suma = 0
for i in range(min(numero1, numero2) + 1, max(numero1, numero2)):     # En el caso del 2do extremo, no lo incluye en la suma
    suma += i

print(f"La suma de los números enteros entre {numero1} y {numero2} es: {suma}")