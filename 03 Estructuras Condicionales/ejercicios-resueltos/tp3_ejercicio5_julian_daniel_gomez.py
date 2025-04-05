stop = ''

while stop != 'X':
    password = input("Ingrese una contraseña: ")
    if 8 <= len(password) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
        
    stop = input("Ingrese 'X' si desea finalizar: ")   