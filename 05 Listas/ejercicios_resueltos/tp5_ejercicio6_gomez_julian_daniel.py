# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

# Armado de la lista
lista = list(range(10, 31, 5))
print(f"Lista de números del 10 al 30 (incluído) con saltos de 5 en 5: {lista}")

# Muestro los dos primeros números
print(f"Los dos primeros números son: {lista[:2]}")
