
numero = int(input("Ingrese su número: "))
divisores = 0
for i in range(2, numero):
    if numero % i == 0:
        divisores += 1
        
if divisores > 0:
    print(f"{numero} no es primo.")
else:
    print(f"{numero} sí es primo.")