
# Parámetros
# Valor de retorno

# Sin parámetros y sin valor de retorno
def suma1():
    # Las variables x, y, suma son variables locales y no se pueden acceder
    # desde fuera de esta función
    x = float(input("Ingrese el valor de x: "))
    y = float(input("Ingrese el valor de y: "))
    suma = x + y
    print(f"El resultado de la suma es: {suma}")

# Sin parámetros y con valor de retorno
def suma2():
    x = float(input("Ingrese el valor de x: "))
    y = float(input("Ingrese el valor de y: "))
    suma = x + y
    # return suma # Regresa una copia del valor de suma
    return x, y, suma # Regresa una tupla que contiene a x,y,suma

# Con parámetros y con valor de retorno
def suma3(x, y):
    x = x + 10
    y = y * 2
    suma = x + y
    return suma
    
# print("Usando suma1()...")
# res = suma1() # suma1() se sustituye por None
# print(res)
# # print(x) # Error
# # print(y) # Error
# # print(suma) # Error
# print("Terminando de usar suma1()...")

# print("Usando suma2()...")
# res = suma2() # suma2() se sustituye por una copia del valor del return suma
# print(res[2])
# a,b,c = suma2()
# print(f"a: {a}, b: {b}, c: {c}")
# print("Terminando de usar suma2()...")

print("Usando suma3()...")
a = float(input("Ingrese x: "))
b = float(input("Ingrese y: "))
res = suma3(a,b)
print(a)
print(b)
print(res)
# res2 = suma3(5+2, 8)
# print(res2)
print("Terminando de usar suma3()...")