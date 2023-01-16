lista = ["Enzo", "Rodolfo", "Danna", "Omar", "Emilio"]

nombre = input("Ingrese el nombre a buscar: ")

encontrado = False
for i in lista:
    if nombre == i:
        encontrado = True

if encontrado:
    print(f"{nombre} está en la lista.")
else:
    print(f"{nombre} no está en la lista.")

# ----------------------------------------
    
for i in lista:
    if nombre == i:
        print(f"{nombre} está en la lista.")
        break
else: # Si no se rompió el ciclo, ejecuta esto
    print(f"{nombre} no está en la lista.")