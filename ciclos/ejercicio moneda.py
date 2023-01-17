import random

ganadas = 0
perdidas = 0
seguir_jugando = 1
while seguir_jugando == 1:
    while (tirada := int(input("Elige 1)Águila, 2)Sol: "))) not in [1,2]:
        print("Debe elegir 1 o 2.")
    moneda = random.randint(1,2)

    if moneda == 1:
        print("La moneda cayó Águila.")
    else:
        print("La moneda cayó Sol.")

    if tirada == moneda:
        print("Atinaste a la moneda.")
        ganadas += 1
    else:
        print("Lo siento, fallaste.")
        perdidas += 1

    while (seguir_jugando := int(input("¿Desea seguir jugando? 1)Sí, 2)No: "))) not in [1,2]:
        print("Debe elegir 1 o 2.")

jugadas = ganadas + perdidas
print(f"Jugaste {jugadas} veces.")
print(f"Atinaste: {ganadas} veces.")
print(f"Fallaste: {perdidas} veces.")