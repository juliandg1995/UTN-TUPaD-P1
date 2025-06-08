# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique.

import fn_import as imp
fn = imp.fn
    
pos = fn.leer_entero_positivo("Ingrese un número entero positivo para calcular la serie de Fibonacci: ")
print(f"El valor de la posición {pos} en la serie Fibonacci es: {fn.fibonacci(pos)}")




    