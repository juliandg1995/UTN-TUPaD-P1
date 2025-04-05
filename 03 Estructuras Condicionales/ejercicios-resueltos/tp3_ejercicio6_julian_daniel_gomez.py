from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) 
                      for i in range(50)]

media = median(numeros_aleatorios)
mediana = mean(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(*numeros_aleatorios, sep='\n')
print("")

if ( media > mediana and mediana > moda ):
      print(f"{media} > {mediana} && {mediana} > {moda}", "\n")
      print("Sesgo positivo o a la derecha", "\n")
elif ( media < mediana and mediana < moda ):
      print("Sesgo negativo o a la izquierda", "\n")
      print(f"{media} < {mediana} && {mediana} < {moda}", "\n")
elif ( media == mediana == moda):
      print(f"{media} == {mediana} == {moda}", "\n")
      print("Sin sesgo", "\n")
else:
      print("Distribución irregular o multimodal", "\n")
