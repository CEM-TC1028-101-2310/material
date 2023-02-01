
with open("ejemplo escritura.txt", "w", encoding="utf8") as archivo:
    # archivo.write(string) -> Escribe el string dentro del archivo
    # y deja el cursor al final de nuestro string.
    archivo.write("hola\n")
    archivo.write("mundo")
    
    archivo.write("""
¿Cómo
estás?
""")
    # archivo.writelines(lista) -> Junta todos los contenidos de la lista
    # y los escribe en el archivo. La lista sólo puede contener strings
    # para que funcione.
    lista = ["Es\n", "un\n", "ejemplo\n", "de\n", "writelines()"]
    archivo.writelines(lista)

print("Terminó de escribir...")