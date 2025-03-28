'''Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
Tener en cuenta la siguiente equivalencia:
𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =95.𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32'''

emp_celcius = round( float( input("Ingrese una temperatura en °C: ") ), 2 )
temp_farenheit = round( ( (9/5) * temp_celcius + 32 ), 2)
print(f"El equivalente a {temp_celcius} °C en grados Farenheit es: {temp_farenheit}")