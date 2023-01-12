# for variable in secuencia:

# range(num)
# Genera una secuencia numérica que inicia en 0, termina
# uno antes de num y avanza de 1 en 1
for i in range(5):
    print(f"El valor de i es: {i}")

print("----------------------")

# range(inicio, final)
# Genera una secuencia numérica que inicia en inicio, termina
# uno antes de final y avanza de 1 en 1
for i in range(3,7):
    print(f"El valor de i es: {i}")
    
print("----------------------")

# Si no se puede generar la secuencia avanzando de 1 en 1,
# se genera una secuencia vacía
for i in range(7,3):
    print(f"El valor de i es: {i}")

print("----------------------")

# range(inicio, final, paso)
# Genera una secuencia numérica que inicia en inicio, termina antes de
# final y avanza de paso en paso
for i in range(4,15,3):
    print(f"El valor de i es: {i}")
    
print("----------------------")

for i in range(7,3,-1):
    print(f"El valor de i es: {i}")
    
print("----------------------")

texto = "hola mundo"
for i in texto:
    print(f"El valor de i es: {i}")
    
print("----------------------")

lista = [1,2,"hola",True,[7,False],5.3]
for i in lista:
    print(f"El valor de i es: {i}")
    
print("----------------------")

tupla = (1,2,"hola",True,[7,False],5.3)
for i in tupla:
    print(f"El valor de i es: {i}")