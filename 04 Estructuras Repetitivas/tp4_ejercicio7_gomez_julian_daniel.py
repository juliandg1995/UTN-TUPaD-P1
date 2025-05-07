# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# Se valida que el valor ingresado sea un número entero positivo.
while True:
    try:
        nro = int(input("Ingrese un número entero positivo: "))
        if nro < 0:
            raise ValueError("El número debe ser positivo.\n")
        break
    except ValueError:
        print("Debe ingresar un número entero positivo.\n")

# Se realiza la suma de los números comprendidos entre 0 y el número ingresado.
suma = 0
for i in range(0,nro+1):
    suma += i

print(f"\nLa suma de los números comprendidos entre 0 y {nro} es: {suma}")