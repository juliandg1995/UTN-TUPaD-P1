stop = ''

while stop != 'X':
    valor = int(input(" Ingrese una magnitud de terremoto: "))
    print("")
    if str(valor) != "":
        print("")     
        if (valor < 3):
            print("Muy leve (Imperceptible)")
        elif (3 <= valor < 4):
            print("Leve (Ligeramente perceptible)")
        elif (4 <= valor < 5):
            print("Moderado (sentido por personas pero generalmente no causa daños)")
        elif(5 <= valor < 6):
            print("Fuerte (puede causar daños en estructuras débiles)")
        elif(6 <= valor < 7 ):
            print("Muy Fuerte (puede causar daños significativos)")
        else:
            print("Extremo (puede causar graves daños a gran escala)")
        
        stop = input("Ingrese 'X' si desea finalizar: ")
        print("")                      
    else:
        print("No ha ingresado ningún valor")