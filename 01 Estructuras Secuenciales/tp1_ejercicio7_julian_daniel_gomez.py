'''Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.'''

nro1 = int( input("Ingrese un nro distinto de 0: ") )
while nro1 == 0:
    nro1 = int( input("Por favor, ingrese un nro distinto de 0: ") )

nro2 = int( input("Ahora ingrese otro nro distinto de 0: ") )
while nro2 == 0:
    nro2 = int( input("Por favor, ingrese un nro distinto de 0: ") )

print(f"{nro1} + {nro2} = {nro1 + nro2}")
print(f"{nro1} - {nro2} = {nro1 - nro2}")
print(f"{nro1} * {nro2} = {nro1 * nro2}")
print(f"{nro1} / {nro2} = {nro1 / nro2}")