edad = int(input("Ingrese su edad: "))
while edad <= 0:
    edad = int(input("Ingrese una edad válida mayor a cero: "))

if edad >= 18:
    print("El usuario es mayor de edad")
else:
    print("El usuario es menor de edad")