# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta-
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
# sultados de forma clara

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions')))
import functions as funciones

nro1 = funciones.ingresar_numero_entero("Ingrese el primer número: ")
nro2 = funciones.ingresar_numero_entero("Ingrese el segundo número: ")

lista_operaciones = funciones.operaciones_basicas(nro1, nro2)

# Imprimo los resultados de las operaciones
for i, operacion in enumerate(["Suma", "Resta", "Multiplicación", "División"]):
    print(f"{operacion}: {lista_operaciones[i]}")
    

    
    