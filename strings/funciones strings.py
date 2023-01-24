
texto = "Hola mundo"
texto = texto.upper() # Generando un nuevo string con el string original en mayúsculas
print(texto)

texto = "Hola mundo"
primera = texto[:len(texto)//2].upper()
segunda = texto[len(texto)//2:]
texto = primera + segunda
print(texto)


texto = "HoLa MuNDO"
# Genera un nuevo string con el contenido del string original en minúsculas
print(texto.lower())

# El contenido está en minúsculas, pero la primera letra de cada palabra es
# mayúscula
print(texto.title())

texto = "Hola mundo"

# string.replace(x,y) -> Reemplaza todas las ocurrencias de x por el substring y
texto = texto.replace("ol", "")
print(texto)

# entrada = input("Dime sí o no: ")
# if entrada.lower().replace(" ", "") in ["sí", "si"]:
#     print("Escribió sí...")
    
# string.strip() quita los espacios vacíos del inicio y el final
# considera como espacios vacíos al espacio normal, al tabulador y al salto de línea
# nombre = input("Escribe tu(s) nombre(s): ")
# nombre = nombre.strip()

# entrada = input("Dime sí o no: ").lower().strip()
# if entrada in ["sí", "si"]:
#     print("Escribió sí...")
# print(nombre)


# string.split(x) -> Separa en una lista los elementos usando x como el valor
# para dividir el string. Si no se proporciona una x, lo hace en base a los
# espacios vacíos.
texto = "Hola mundo, ¿cómo estás?"
lista = texto.split("o")
print(lista)

# string.join(list) -> Junta el contenido de una lista y toma al string
# como separador entre los elementos de la lista. NOTA: El contenido
# de la lista deben ser sólo strings.
lista = ["Hola", "mundo", "aquí", "estoy"]
texto = ", ".join(lista)
print(texto)

# string.count(x) -> Indica cuántas veces aparece x dentro del string
texto = "Hola mundo, ¿cómo estás?"
print(texto.count(" "))

# x in string -> Indica si x aparece en string (True, False)
# x not in string -> Indica si x no aparece en string (True, False)
print("mundo" in texto)
print("mundo" not in texto)

# string.find(x) y string.index(x) -> Busca la primera ocurrencia de x
# dentro del string y nos da el índice en la que se encuentra.
# NOTA: Si x no existe dentro de string, find regresa -1 e index
# arroja un error.
print(texto.find("a"))
print(texto.index("a"))

print(texto.find("x"))
# print(texto.index("x"))

# Pregunta si un string inicia y termina con un substring
print(texto.startswith("Hola"))
print(texto.endswith("Hola"))

# Indica si todos los caracteres del string pertenece al alfabeto
texto = "hola"
print(texto.isalpha())

# Indica si todos los caracteres del string son números
texto = "345678.183"
print(texto.isnumeric())

# Indica si todos los caracteres del string son alfanuméricos
texto = "4567asnsdj56"
print(texto.isalnum())

# Obtiene el valor de la tabla unicode del caracter
a = "a"
print(ord(a))

# Obtiene el valor de caracter respecto al valor numérico proporcionado
# en la tabla unicode
a = 97
print(chr(a))
