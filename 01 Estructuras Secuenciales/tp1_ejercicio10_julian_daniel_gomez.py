'''Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.'''
import array 

cant_nros = 3

num_array = array.array('i', [0] * cant_nros)
for i in range(0, cant_nros):
    num_array[i] = int(input(f"Ingrese el número {i + 1}: "))

print(f"El promedio de los números {num_array[0]}, {num_array[1]} y {num_array[2]} es: {sum(num_array)/len(num_array)}")