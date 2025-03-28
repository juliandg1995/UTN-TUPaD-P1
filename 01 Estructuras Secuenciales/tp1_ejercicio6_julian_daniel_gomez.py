''' Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número. '''

nro = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{nro} * {i} = {nro * i}")


