nota = int(input("Ingrese su nota: "))

while nota <= 0 or nota > 10:
    nota = int(input("Ingrese una nota válida mayor a cero y no mayor que 10: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")