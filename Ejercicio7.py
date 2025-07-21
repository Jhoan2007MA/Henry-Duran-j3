# Hacer un rpograma que determine si una palabra ingresada es un palindromo
# (Se lee igual al derecho y al reves)
# Utilizando slicing 

palabra = input("Escribe una palabra: ").lower()
invertida = palabra[::-1]

if palabra == invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")