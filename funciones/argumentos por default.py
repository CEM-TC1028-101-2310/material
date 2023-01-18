
# def suma(x: int, y: int ,z: int) -> int: # Anotaciones para sugerir los tipos de datos
def suma(x, y = 15, z = 12):
    return x + y + z

r = suma(7,3,1)
print(r)

r = suma(y=6, x=12, z=28)
print(r)

r = suma(2,z=3,y=15)
print(r)

# r = suma(x=2,z=3,15) # Error, espera que los argumentos posicionales sean los primeros en ser mandados
# print(r)

r = suma("hola", "mundo", "¿cómo estás?")
print(r)

r = suma(10, 5)
print(r)

r = suma(10, z = 15)
print(r)

print("Hola", "mundo", sep=" -+- ", end="***")
print("Hey")