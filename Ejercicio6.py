# Hacer un programa que tome un numero de telefono ingresado (10 digitos) y 
# Lo formatee como (xxx) xxx-xxxx
# Utilizando f-strings 

telefono = input("Escribe un número de teléfono de 10 dígitos: ")
if len(telefono) == 10 and telefono.isdigit():
    telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"
    print(f"El número formateado es: {telefono_formateado}")
else:
    print("El número debe tener exactamente 10 dígitos.")