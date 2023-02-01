import csv

lista = []
with open("boleta.csv", "r", encoding="utf8") as archivo:
    lector = csv.reader(archivo)
    for linea in lector:
        if linea[0] == "Alberto":
            lista.append(["Alberto", 80])
        else:
            lista.append(linea)

with open("boleta.csv", "w", encoding="utf8", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(lista)
    
print("Terminó...")