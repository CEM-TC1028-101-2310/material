import csv

with open("boleta.csv", "r", encoding="utf8") as archivo:
    lector = csv.reader(archivo)
    promedio = 0
    cont = 0
    for linea in lector:
        print(linea)
        if "Melendez, Emilio" == linea[0]:
            print("Lo encontré...")
        if cont > 0:
            promedio += float(linea[1])
        cont += 1
    promedio /= cont
    print(f"El promedio es: {promedio}")
            
print("-----")            

with open("boleta.csv", "r", encoding="utf8") as archivo:
    lector = csv.DictReader(archivo)
    promedio = 0
    cont = 0
    for linea in lector:
        print(linea)
        if "Melendez, Emilio" == linea["Nombre"]:
            print(linea["Calificación"])
            print("Lo encontré...")
        promedio += float(linea["Calificación"])
        cont += 1
    promedio /= cont
    print(f"El promedio es: {promedio}")