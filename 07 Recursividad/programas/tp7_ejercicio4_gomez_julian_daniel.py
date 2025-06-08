# Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛∗𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general.

import fn_import as imp
fn = imp.fn

decimal = fn.leer_entero_positivo("Ingrese un numero en decimal para convertirlo a binario : ")
binario = fn.decimal_a_binario(decimal)
print(f"El número en decimal {decimal} convertido en binario es: {binario}")