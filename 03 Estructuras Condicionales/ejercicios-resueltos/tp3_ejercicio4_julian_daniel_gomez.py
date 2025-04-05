stop = ''

while stop != 'X':
    edad = int(input("Ingrese una edad: "))
    if edad < 12:
        print("Niño/a")
    elif 12 <= edad < 18:
        print("Adolescente")
    elif 18 <= edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")
        
    stop = input("Ingrese 'X' si desea finalizar: ")    