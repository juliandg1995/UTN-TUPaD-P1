'''Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.'''

segundos = int( input("Ingrese una cantidad de segundos: ") )
hora = segundos / 3600
print(f"La cantidad de {segundos} segundos equivale a {hora: .2f} horas")