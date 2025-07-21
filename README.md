Ejercicio 1: Contando caracteres 
introduccion:
Realizamos un programa que le pida al usuario una frase y muestre, 1. la cantidad de caracteres en la frase y 2. la cantidad de espacios en la frase.
utilizando la funcion len() que nos permite contar cuantos caracteres tiene una frase
utilizando la funcion count() que nos cuenta cuantos espacios tiene una frase. 
como ejemplo observamos lo siguiente: 

frase = input("Escribe una frase: ")
total_caracteres = len(frase)
espacios = frase.count(" ") 
si engresamos una frase como : programacion.
nos dira que tiene 12 caracteres y 0 espacios. 

Ejercicio 2: Validando nombres
introduccion: 
Realizar un programa que le pida al usuario su nombre completo y que verifique que todas las iniciales esten en mayusculas.
y que solo contengan letras. 
Utilizando la funcion isalpha() que nos ayuda a verificar que solo hayan letras.
Utilizando la funcion istitle() que nos ayuda a verificar que las palabras comiencen con mayusculas. 
como ejemplo podemos oberservar lo siguiente: 

nombre = input("Escribe tu nombre completo: ")

if nombre.replace(" ", "").isalpha():
    if nombre.istitle():
        print("El nombre es válido.")
    else:
        print("El nombre debe comenzar con mayúscula.")
else:
    print("El nombre solo debe contener letras.")

Ejercicio 3: Invirtiendo palabras
introduccion: 
Crear un programa en donde le pida al usuario una palabra y muestre la palabra invertida.
Utilizando el operador slicing [:: -1] para invertir la cadena.
podemos observar el siguiente ejemplo: 

palabra = input("Escribe una palabra: ")
invertida = palabra[::-1]
print(f"La palabra invertida es: {invertida}")

Ejercicio 4: Cifrando texto
introduccion: 
Reaalizar un programa que le pida al usuario una palabra el cual pueda cambiar las vocales por (*)
Utilizando replace() tanto en vocales minusculas como mayuculas tambien.
EJEMPLO: 
frase = input("Escribe una frase: ")

frase_cifrada = frase.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")
frase_cifrada = frase_cifrada.replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")

print(f"La frase cifrada es: {frase_cifrada}")

Ejercicio 5: Contador de vocales
 Instruduccion: 
 Realiza un programa que pueda indentificar las vocales y hacer la sumatoria de las vocales.
 Utilizando la funcion count() podemos hacer la cuenta de cuantas palabras tiene la frase ingresada
 Utilizando matematica basica hacemos la suma de las vocales. 
 COMO POR EJEMPLO: 

 frase = input("Escribe una frase: ")

a = frase.count("a") + frase.count("A")
e = frase.count("e") + frase.count("E")
i = frase.count("i") + frase.count("I")
o = frase.count("o") + frase.count("O")
u = frase.count("u") + frase.count("U")

total_vocales = a + e + i + o + u

print(f"La frase tiene {total_vocales} vocales.")

Ejercicio 6: Formateando cadenas
Introduccion: 
Crea un programa el cual le pida un numero al usuario de 10 digitos y este lo formatee como (xxx) xxx xxxx
Utilizando silcling [:: -1] para divir las cadenas en partes.
Utilizando el f-strings 
podemos observar el siguiente ejemplo : 

telefono = input("Escribe un número de teléfono de 10 dígitos: ")
if len(telefono) == 10 and telefono.isdigit():
    telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"
    print(f"El número formateado es: {telefono_formateado}")
else:
    print("El número debe tener exactamente 10 dígitos.")

Ejercicio 7: Detectando palíndromos
introduccion: 
Hacer un pograma  que determine si una palabra ingresada por el usuario es un palíndromo (se lee igual al derecho y al revés).
Usa slicing para invertir la palabra.
 Compara la palabra original con la invertida.
 podemos observar el siguiente ejemplo : 

 palabra = input("Escribe una palabra: ").lower()
invertida = palabra[::-1]

if palabra == invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.").
