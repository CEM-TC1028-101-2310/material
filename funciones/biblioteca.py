
def suma(x,y):
    return x + y

def resta(x,y):
    return x - y

# sólo en caso de que se ejecute directamente este archivo
# se haga lo siguiente:
if __name__ == "__main__": 
    print("Dentro de biblioteca.py...")
    print(__name__)
    res = resta(10,5)
    print(f"Resta: {res}")
