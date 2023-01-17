
cuenta = 0

# precio = 0
# while precio >= 0:
#     cuenta += precio
#     precio = float(input("Ingrese el precio del producto: "))

while (precio := float(input("Ingrese el precio del producto: "))) >= 0:
    cuenta += precio
    
print(f"El total de la cuenta fue: ${cuenta:,.2f}")