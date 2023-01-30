
A = [[-2,5,6],
     [5,2,7]]

print(A)
print(A[1][2])

# len(A) -> número de filas
# len(A[0]) -> número de columnas

# Recorrido por filas
for fila in range(len(A)):
    for columna in range(len(A[0])):
        print(f"A[{fila}][{columna}] = {A[fila][columna]}")

print("-"*10)

# Recorrido por columnas
for columna in range(len(A[0])):
    for fila in range(len(A)):
        print(f"A[{fila}][{columna}] = {A[fila][columna]}")
    
    