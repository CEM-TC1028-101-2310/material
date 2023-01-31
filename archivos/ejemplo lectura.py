
archivo = open("ejemplo lectura.txt", "r", encoding="utf8")

# archivo.read() -> Lee todo el contenido del archivo a partir de donde está
# ubicado el cursor hasta el final del archivo. Deja al cursor al final del archivo.
# NOTA: No se recomienda utilizar con archivos muy grandes.
# contenido = archivo.read()
# print(contenido)
# print("-------")
# # El cursor ya está en el final del archivo, por lo que el segundo read
# # no obtiene contenido.
# contenido = archivo.read()
# print(contenido)

# archivo.readline() -> Lee el contenido de la línea actual y deja el cursor
# al inicio de la siguiente línea
# NOTA: Cada línea contiene a su salto de línea \n
# linea = archivo.readline()
# linea = archivo.readline()
# linea = archivo.readline()
# print(linea)

# archivo.readlines() -> Lee todo el contenido del archivo y lo separa en
# líneas que introduce en una lista que da como resultado.
# NOTA: No se recomienda usar en caso de tener un archivo muy grande.
# lineas = archivo.readlines()
# print(lineas)

suma = 0
for linea in archivo:
    print(f"Mi línea es: {linea.strip()}")
    suma += float(linea)
print(suma)

archivo.close()