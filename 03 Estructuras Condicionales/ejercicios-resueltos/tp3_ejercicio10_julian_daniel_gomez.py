stop = ''

while stop != 'X':
    hemisferio = input(" Ingrese el hemisferio (N o S): ")
    print("")
    if not("S" != hemisferio != "N"):
        print("")
        dia = int(input("Ingrese el dia del mes: "))
        while not(0 < dia <= 31):
            dia = int(input("Ingrese un día válido: "))
        mes = int(input("Ingrese el mes (del 1 al 12): "))
        while not(0 < mes <= 12):
            mes = int(input("Ingrese un mes válido: "))

        # Diciembre-Marzo
        if (mes == 12 and dia >= 21 ) or (1 <= mes <=2 ) or (mes == 3 and dia <= 20):
            if (hemisferio == "S"):
                estacion = "Verano"
            else:
                estacion = "Invierno"
        # Marzo - Junio
        elif ( mes == 3 and dia >= 21 ) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
            if (hemisferio == "S"):
                estacion = "Otoño"
            else:
                estacion = "Primavera"

        # Junio - Septiembre
        elif ( mes == 6 and dia >= 21 ) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
            if (hemisferio == "S"):
                estacion = "Invierno"
            else:
                estacion = "Verano"
        else:
            if (hemisferio == "S"):
                estacion = "Primavera"
            else:
                estacion = "Otoño"        

        print(f"Actualmente usted se encuentra en la estación de {estacion}\n")

        stop = input("Ingrese 'X' si desea finalizar: ")
        print("")                      
    else:
        print("Ingrese un hemisferio válido (N o S): ", "\n")