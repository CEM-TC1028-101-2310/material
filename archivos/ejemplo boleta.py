
with open("boleta.csv", "r", encoding="utf8") as archivo:
    for linea in archivo:
        lista = linea.split(",")
        print(lista)
        if lista[0] == "Emilio":
            print(f"La calificación de Emilio es: {lista[1].strip()}")
print("-----")