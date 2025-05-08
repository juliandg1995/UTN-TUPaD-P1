# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
# Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []

lista= []

for i in range(3):
    palabra = input(f"Ingrese la palabra {i+1}: ")
    lista.append(palabra)

print(f"\nLista de palabras: {lista}")