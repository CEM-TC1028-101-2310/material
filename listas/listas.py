
lista = []
print(lista)

lista = ["hola", 12, 5.8, [True, False], (5,2)]
print(lista)

lista = [1,2] + [3,4]
print(lista)

lista = [0] * 3
print(lista)

# list comprehension
lista = [i**2 for i in range(15,21)]
print(lista)

lista = ["hola", 12, 5.8, [True, ["otro", "nivel"], False], (5,2)]
print(lista[2])
print(lista[-3])

print(lista[3])
print(lista[3][1])
print(lista[3][1][1])

# Slicing
# lista[inicio:final:paso]
# Nunca toca al valor de final
# Si se omite inicio o final, va desde el principio o hasta el final
# dependiendo de cual se omitió
# Si se omite el paso, va de 1 en 1
print(lista[2:4])
print(lista[:4])
print(lista[2:])
print(lista[:])
print(lista[2:4:2])
print(lista[::-1])

lista = [1,4,True,"hola",7.2]
lista[-2] = False
print(lista)

