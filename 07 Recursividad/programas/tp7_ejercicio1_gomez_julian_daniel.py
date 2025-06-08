# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

import fn_import as imp
fn = imp.fn
    
numero = fn.leer_entero_positivo("Ingrese un número entero positivo para calcular su factorial: ")
print(f"El factorial de {numero} es: {fn.factorial(numero)}")


    