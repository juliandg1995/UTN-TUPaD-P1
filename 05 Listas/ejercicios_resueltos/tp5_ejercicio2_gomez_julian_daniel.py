# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

lista_random = [1, 2.5, True, "Texto", ["a", 2, False]]

print(f"El penúltimo elemento de la lista es: {lista_random[-2]}\n")

# Alternativa sin usar index negativo
# print(f"El penúltimo elemento de la lista es: {lista_random[len(lista_random) - 2]}\n")