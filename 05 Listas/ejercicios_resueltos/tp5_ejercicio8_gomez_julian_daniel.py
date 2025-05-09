# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.

# Lista vacía
dobles = [] 

# Agrego elementos usando un array en vez de un rango dinámico en el for
for i in [5, 10, 15]:
    dobles.append(i * 2)

# Imprimo lista:
print(f"\nLista:\n{dobles}\n")
