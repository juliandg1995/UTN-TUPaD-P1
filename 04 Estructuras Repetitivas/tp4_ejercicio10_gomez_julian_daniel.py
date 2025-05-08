#  Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

while True:
    try:
        numero = int(input("Ingrese un número a procesar: "))
        break
    except ValueError:
        print("Debe ingresar un número entero.\n")

new_string = ' '

while numero > 0:
    digito = numero % 10        # Se obtiene el último dígito aplicando el modulo del número
    new_string += str(digito)   # Se convierte el dígito a string
    numero = numero // 10       # Se elimina el último dígito dividiendo el número por 10 y redondeando hacia abajo

print(f"\nEl número invertido es: {new_string}")
