lista = [1,2,True,"hola"]

# Métodos o procedimientos para modificar listas

# lista.append(elemento)
# Agrega un elemento hasta el final de la lista
lista.append("mundo")
print(lista)

x = 15
lista.append(x)
print(lista)
x = 80
print(x)
print(lista)

# lista.insert(posición, valor)
# Agrega el valor en la posición y lo demás lo recorre a la derecha
lista.insert(3,5)
print(lista)

# Si el índice positivo no existe, se agrega al final
lista.insert(20, "hola")
print("-", lista)

# Si el índice negativo no existe, se agrega al inicio
lista.insert(-20, "prueba")
print(lista)

# lista.pop() es una función y no un procedimiento/método
# lista.pop(índice)
# Saca un elemento de la lista y lo devuelve como valor de retorno
# Si pop no tiene argumentos, el elemento que saca es el último de la lista
# Si pop tiene un argumento entero, se saca el que se encuentra en ese índice
elemento = lista.pop()
print(lista)
print(elemento)

elemento = lista.pop(2)
print(lista)
print(elemento)

# Si el índice no existe en la lista, marca un error
# print(lista.pop(10))

# lista.remove(elemento)
# Se elimina la primera ocurrencia (de izquierda a derecha) de elemento que aparece
# dentro de la lista
lista.append("hola")
print(lista)
lista.remove("hola")
print(lista)

lista = [1,2, ["hola", "adios"], True]
lista[2].pop()
print(lista)

# Si el elemento no existe en la lista, marca un error
# lista.remove("cualquier cosa")

# Revisando que se puedan eliminar los elementos en la lista

# lista.pop()
lista = [1,2,"hola",True]
indice = -6
if indice < 0:
    if indice >= -len(lista):
        lista.pop(indice)
else:
    if indice < len(lista):
        lista.pop(indice)
        
# lista.remove()
lista = [1,2,"hola",True]
elemento = "un elemento"
if elemento in lista:
    lista.remove(elemento)

lista = [1,2,2,2,3,4,6,3,2,1]

# lista.count(elemento) -> Indica la cantidad de ocurrencias del elemento en la lista
print(lista.count(2))

# lista.index(elemento) -> Indica la posición de la primera ocurrencia del
# elemento en la lista. Si no lo encuentra, marca error.
if 2 in lista:
    print(lista.index(2))
    
indices = []
for indice,valor in enumerate(lista):
    if valor == 2:
        indices.append(indice)
print(indices)


lista = [1,4,42,1,5,6,3,2,5,3,1]

# Invierte el orden de la lista
lista.reverse()
print(lista)

# Ordena los valores de menor a mayor
lista.sort()
print(lista)

# Ordena los valores de mayor a menor
lista.sort(reverse=True)
print(lista)

lista = ["casa", "alejandro", "ahora", "Xochimilco" , "elefante", "perro"]
# Si la lista contiene strings, se ordena en base al valor en la tabla unicode
lista.sort()
print(lista)

# NOTA: No se pueden mezclar los tipos de datos de la lista porque marca error
# lista = ["casa", 1, 3, "hola"]
# lista.sort()
# print(lista)

lista = [1,2,3,4,5]
print(sum(lista))
print(min(lista))
print(max(lista))
print(sum(lista)/len(lista))

a = 5
b = a + 10
a = 7
print(a, b)


# b es otro nombre para a
a = [1,2,3]
b = a
a.append(5)
b.append(10)
print(a)
print(b)

# b es una copia del contenido de a
a = [1,2,3]
b = a.copy()
a.append(5)
b.append(10)
print(a)
print(b)