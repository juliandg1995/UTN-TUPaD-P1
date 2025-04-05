stop = ''
vocales = ['a','e','i','o','u']

while stop != 'X':
    str = input("Ingrese una palabra o frase ")
    if str != "":
        if str[len(str) - 1] in vocales:
            print(f"{str}!", "\n")
        else:
            print(str, "\n")
        
    stop = input("Ingrese 'X' si desea finalizar: ")  