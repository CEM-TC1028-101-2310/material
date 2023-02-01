import csv

with open("boleta.csv", "a", encoding="utf8", newline="") as archivo:
    escritor = csv.writer(archivo)
    alumno = ["Alberto", 88]
    escritor.writerow(alumno)
print("Terminó de escribir...")

with open("boleta.csv", "a", encoding="utf8", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["Nombre", "Calificación"])
    escritor.writerow({
        "Nombre": "Enzo",
        "Calificación": 95
        })
print("Terminó de escribir...")