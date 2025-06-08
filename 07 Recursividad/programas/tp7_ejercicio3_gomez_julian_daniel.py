# Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛∗𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general.

import fn_import as imp
fn = imp.fn

base = fn.leer_entero_positivo("Ingrese una base positiva: ")
exp = fn.leer_entero_positivo("Ingrese un exponente positivo: ")

print(f"El resultado de elevar {base} a la {exp} es: {fn.potencia(base,exp)}")
