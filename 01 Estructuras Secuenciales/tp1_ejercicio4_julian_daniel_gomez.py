'''Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.'''

from math import pi

radio = float(input("Ingrese el radio de un círculo: \n"))

perimetro = 2 * pi * radio
area = pi * pow(radio, 2)
print(f"El perímetro de un círculo con radio {radio} cm, es de {perimetro: .3f} cm\n")
print(f"El área de un cículo con radio {radio} cm es de {area: .3f} cm2 \n")