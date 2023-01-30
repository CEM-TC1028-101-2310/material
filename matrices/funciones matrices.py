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
    matriz2 = [[6,3,2], [6,2,5], [4,2,1]]
    
    print(dimensiones_matriz(matriz1))
    print(dimensiones_matriz(matriz2))
    print(comparacion_dimensiones(matriz1, matriz2))
    
    res = suma_filas(matriz2)
    print(res)
    
    