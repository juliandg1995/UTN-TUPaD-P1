# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

# Se ingresa la cantidad de números a procesar, se valida que sea un número entero positivo.
while True:
    try:
        cant_input = int(input("Ingrese la cantidad de números a procesar: "))
        break
    except ValueError:
        print("Debe ingresar un número entero positivo.\n")

cantidad_numeros = 0
suma = 0

# Se utiliza un bucle for para iterar 100 veces, permitiendo al usuario ingresar un número entero en cada iteración.
# Se valida que el valor ingresado sea un número entero.
for i in range(cant_input):
    while True:
        try:
            nro = int(input(f"\nIngrese el número {i+1}: "))
            break
        except ValueError:
            print("Debe ingresar un número entero.\n")
            
    cantidad_numeros += 1
    suma += nro

# Se imprime el resultado utilizando dos posiciones decimales para el promedio (:.2f).
print(f"\nLa media de los números ingresados es: {suma / cantidad_numeros:.2f}\n")
    