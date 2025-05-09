# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 
# autos = ["sedan", "polo", "suran", "gol"]

# Lista original
autos = ["sedan", "polo", "suran", "gol"]
print(f"\nLista original:\n{autos}\n")

# Reemplazo los valores en los índices 1 y 2
autos[1:3] = ["camioneta", "pickup"]
print(f"Lista de autos modificada:\n{autos}\n")