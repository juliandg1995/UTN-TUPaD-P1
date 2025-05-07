# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

while True:
    try:
        cant_input = int(input("Ingrese la cantidad de números a procesar: "))
        break
    except ValueError:
        print("Debe ingresar un número entero positivo.\n")

par = 0
impar = 0
positivo = 0
negativo = 0

# Se utiliza un bucle for para iterar 100 veces, permitiendo al usuario ingresar un número entero en cada iteración.
# Se valida que el valor ingresado sea un número entero.
for i in range(cant_input):
    while True:
        try:
            nro = int(input(f"\nIngrese el número {i+1}: "))
            break
        except ValueError:
            print("Debe ingresar un número entero.\n")

    if nro % 2 == 0:
        par += 1
    else:
        impar += 1

    if nro < 0:
        negativo += 1
    else:
        positivo += 1

# Imprimo el resultado con la info de todos los contadores
print(f"""\n
La cantidad de números pares es: {par}\n
La cantidad de números impares es: {impar}\n
La cantidad de números positivos es: {positivo}\n
La cantidad de números negativos es: {negativo}\n""")