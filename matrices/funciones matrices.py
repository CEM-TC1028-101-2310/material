def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def dimensiones_matriz(matriz):
    return [len(matriz), len(matriz[0])]

def comparacion_dimensiones(matriz1, matriz2):
    return dimensiones_matriz(matriz1) == dimensiones_matriz(matriz2)

def suma_filas(matriz):
    res = [0 for i in range(len(matriz[0]))]
    for columna in range(len(matriz[0])):
        for fila in range(len(matriz)):
            res[columna] += matriz[fila][columna]
    return res

def suma_columnas(matriz):
    # Les queda de tarea
    pass

def suma_matrices(matriz1, matriz2):
    if not comparacion_dimensiones(matriz1, matriz2):
        print("Las matrices tienen dimensiones distintas.")
        return False
    filas, columnas = dimensiones_matriz(matriz1)
    res = [[0 for columna in range(columnas)] for fila in range(filas)]
    for fila in range(filas):
        for columna in range(columnas):
            res[fila][columna] = matriz1[fila][columna] + matriz2[fila][columna]
    return res

def resta_matrices(matriz1, matriz2):
    if not comparacion_dimensiones(matriz1, matriz2):
        print("Las matrices tienen dimensiones distintas.")
        return False
    filas, columnas = dimensiones_matriz(matriz1)
    res = [[0 for columna in range(columnas)] for fila in range(filas)]
    for fila in range(filas):
        for columna in range(columnas):
            res[fila][columna] = matriz1[fila][columna] - matriz2[fila][columna]
    return res

def multiplicacion_estandar(matriz1, matriz2):
    f1, c1 = dimensiones_matriz(matriz1)
    f2, c2 = dimensiones_matriz(matriz2)
    if c1 != f2:
        print("Error, no coinciden las columnas de la matriz1 con las filas de la matriz2.")
        return False
    res = [[0 for columna in range(c2)] for fila in range(f1)]
    for fila in range(f1):
        for columna in range(c2):
            for i in range(c1):
                res[fila][columna] += matriz1[fila][i] * matriz2[i][columna]
    return res

if __name__ == "__main__":
#     filas = int(input("Ingrese el número de filas: "))
#     columnas = int(input("Ingrese el número de columnas: "))
    
    # NOTA: No se generan copias de listas para las filas
    # Sólo son referencias a la primera fila
    # Si se cambia una, cambian todas
    # matriz =  [[0] * columnas] * filas
    # matriz[0][1] = 20
    
#     matriz = [[0 for i in range(columnas)] for j in range(filas)]
#     
#     for fila in range(len(matriz)):
#         for columna in range(len(matriz[0])):
#             matriz[fila][columna] = float(input(f"Ingrese el valor de la posición [{fila}][{columna}]: "))
#     imprimir_matriz(matriz)
    matriz1 = [[1,2,3], [4,5,6]]
    matriz2 = [[6,3,2], [6,2,5]]
    
    print(dimensiones_matriz(matriz1))
    print(dimensiones_matriz(matriz2))
    print(comparacion_dimensiones(matriz1, matriz2))
    
    res = suma_filas(matriz2)
    print(res)
    
    res = suma_matrices(matriz1, matriz2)
    imprimir_matriz(res)
    
    A = [[1,2,3], [4,5,6]]
    B = [[9,8], [7,6], [5,4]]
    
    res = multiplicacion_estandar(A,B)
    imprimir_matriz(res)
    