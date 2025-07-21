# Crear un programa en donde se ingrese una frase y se cambien las vocales
# por un caracter especial (*)
# Utilizando replace()

frase = input('Ingrese la frase : ')
frase_cifrada = frase.replace("a","*").replace("e","*").replace("i","*").replace("o","*").replace("u","*")
frase_cifrada = frase.replace("A","*").replace("E","*").replace("I","*").replace("O","*").replace("U","*")
print(f'La frase cifrada es :  {frase_cifrada}')