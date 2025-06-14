# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
#      Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 
# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5)

import fn_import as imp
fn = imp.fn

numero = fn.leer_entero_positivo("Ingrese un numero entero positivo: ")
print(f"La suma de todos los dígitos en {numero} es de: {fn.suma_digitos(numero)}")