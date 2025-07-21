# Hacer un programa que pida el nombre completo y verifique:
# Que solo tenga letras y que comience por mayusculas.
# Utilizando islapha() y istitle()

nombre = input('Ingrese su nombre completo : ')
if nombre.replace(" ", "").isalpha():
    if nombre.istitle():
        print('El nombre es valido ')
    else:
        print('El nombre debe de comenzar en mayuscula.')
else: 
    print('El nombre solo debe de contener letras.')