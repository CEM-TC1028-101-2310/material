print(type(123)) # int -> integer -> número entero
print(type(57.2)) # float -> punto flotante -> número real
print(type(74j)) # complex -> número complejo -> parte real y parte imaginaria
print(type("2345")) # str -> string -> texto
print(type('2345')) # str -> string -> texto
print(type([1,2,"hola",True])) # list -> lista -> conjunto ordenado y mutable de datos
print(type((1,2,"hola",True))) # tuple -> tupla -> conjunto ordenado e inmutable de datos
print(type({"hola": 123, 47: [1,2]})) # dict -> diccionario

lista = [5,3]
print(lista[0])

diccionario = {"hola": 123, 456: [1,2]}
print(diccionario["hola"])
print(diccionario[456])

print(type(True)) # bool -> boolean -> verdadero
print(type(False)) # bool -> boolean -> falso
