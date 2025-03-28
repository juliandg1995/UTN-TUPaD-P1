'''Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2'''

altura = round( float( input("Ingrese su altura en metros: ") ), 2 )
peso = round( float( input("Ingrese su peso en Kg: ") ), 2 )
masa_corporal = round((peso/pow(altura, 2)), 2)
print(f"De acuerdo a la información ingresada, su índice de masa corporal es de {masa_corporal}")
