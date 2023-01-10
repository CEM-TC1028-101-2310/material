import random

print("""Opciones:
1) Debajo de siete.
2) Siete.
3) Arriba de siete.""")

opcion = int(input("Elige tu opción: "))

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

suma = dado1 + dado2

print(f"El dado 1 salió: {dado1}")
print(f"El dado 2 salió: {dado2}")
print(f"La suma de los dados fue: {suma}")

if (opcion == 1 and suma < 7) or (opcion == 2 and suma == 7) or (opcion == 3 and suma > 7):
    print("Ganaste")
else:
    print("Perdiste")

if opcion == 1 and suma < 7:
    print("Ganaste")
elif opcion == 2 and suma == 7:
    print("Ganaste")
elif opcion == 3 and suma > 7:
    print("Ganaste")
else:
    print("Perdiste")