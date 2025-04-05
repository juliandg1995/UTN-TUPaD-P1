stop = ''

while stop != 'X':
    str = input(" Ingrese su nombre: ")
    print("")
    if str != "":
        nro = input("Ingrese un número: ")
        print("")
        if (nro != ""):          
            match nro:
                case '1':
                    print(str.lower())
                case '2':
                    print(str.upper())
                case '3':
                    print(str.capitalize())
                case others:
                    print("Ingrese un número válido", "\n")
            stop = input("Ingrese 'X' si desea finalizar: ")
            print("")                      
    else:
        print("No ha ingresado ningún valor")