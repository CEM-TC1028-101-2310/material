
def funcion(lista):
    # Métodos de listas modifican la lista externa
#     lista.append("hola")
#     lista.append("mundo")
    # Asignaciones no modifican la lista
    # lista = [5,2] + ["hola"]
    
    # Si necesito utilizar alguno de los métodos sin alterar la lista
    # que está fuera de la función, primero debo hacer una copia de
    # la lista original
    lista = lista.copy()
    lista.append("hola")
    lista.append("mundo")
    
if __name__ == "__main__":
    lis = [1,2]
    funcion(lis)
    print(lis)