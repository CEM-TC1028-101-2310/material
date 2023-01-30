
def n_menores(lista: list, numero: int) -> list:
    lista = lista.copy()
    lista.sort()
#     res = []
#     for i in range(numero):
#         res.append(lista[i])
#     return res
    return lista[:numero]

def eliminar_ocurrencias(lista: list, elemento) -> list:
#     lista = lista.copy()
#     while elemento in lista:
#         lista.remove(elemento)
#     return lista

    res = []
    for i in lista:
        if i != elemento:
            res.append(i)
    return res

def eliminar_duplicados(lista: list) -> list:
    res = []
    for i in lista:
        if i not in res:
            res.append(i)
    return res

def k_elementos(lista: list, numero: int) -> list:
    return lista[::numero]
    
if __name__ == "__main__":
    lista = [1,4,6,3,2,5,1,3]
    num = 4
    resultado = n_menores(lista, num)
    print(f"n_menores: {resultado}") # [1,1,2,3]
    
    lista = [1,2,4,2,1,2,4,5,3,2]
    elemento = 2
    resultado = eliminar_ocurrencias(lista, elemento)
    print(f"eliminar_ocurrencias: {resultado}")
    
    lista = [1,3,5,2,1,3,2,8,1,3,5,2,1]
    resultado = eliminar_duplicados(lista)
    print(f"eliminar_duplicados: {resultado}") # [1,3,5,2,8]
    
    lista = [1,2,3,4,5,6,7,8,9]
    num = 3
    resultado = k_elementos(lista, num)
    print(f"k_elementos: {resultado}")