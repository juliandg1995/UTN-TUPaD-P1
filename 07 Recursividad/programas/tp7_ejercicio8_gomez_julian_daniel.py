# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número. 
#       Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4 
# contar_digito(123456, 7)     → 0 

import fn_import as imp
fn = imp.fn

numero = fn.leer_entero_positivo("Ingrese un numero entero positivo: ")
digito = fn.leer_entero_positivo("Ingrese un dígito: ")
print(f"La la cantidad de veces que {digito} aparece en {numero} es de: {fn.contar_digito(numero, digito)}")