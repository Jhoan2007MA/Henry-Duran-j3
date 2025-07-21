# Hacer un programa en donde ingresemos una frase
# Y nos cuente el numero de caracteres y espacios que contenga la frase
# Utilizando len() y count()

frase = input('Ingrese una frase : ')
total_caracteres = len(frase)
espacios = frase.count(" ")
print(f'La frase tiene {total_caracteres} caracteres ')
print(f'La frase tiene {espacios} espacios ')