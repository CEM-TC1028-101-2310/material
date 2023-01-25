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
