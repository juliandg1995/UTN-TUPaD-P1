# Como no se puede importar desde otro directorio indicando el path con barras invertidas de manera 
# directa, hay que hacer este menjunje:
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions')))
import functions as funciones

#Saludo a usuario
funciones.saludo_usuario(input("Ingrese un nombre: "))