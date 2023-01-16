# while condición_de_paro:

# for i in range(5):

i = 0 # inicio
while i <= 4: # final -> condición de paro
    print(f"El valor de i es: {i}")
    # i = i + 1
    i += 1 # paso
    
print("-----------------------")

# for i in range(10,5,-1):

i = 10 # inicio
while i > 5: # final -> condición de paro
    print(f"El valor de i es: {i}")
    # i = i - 1
    i -= 1 # paso

print("-----------------------")

texto = "hola mundo"

# for i in texto:
i = 0
while i < len(texto):
    print(f"i: {i} - texto[i]: {texto[i]}")
    i += 1

print("-----------------------")

lista = [1,5.3,True,[1,6,3],"hola"]

i = len(lista) - 1
while i >= 0:
    print(f"i: {i} - lista[i]: {lista[i]}")
    i -= 1
    
print("-----------------------")

# variable de control, variable centinela
continuar = input("¿Desea continuar s/n?: ")
while continuar != "s":
    continuar = input("¿Desea continuar s/n?: ")




