# match case

print("""Menú:
1) Opción 1
2) Opción 2
3) Opción 3""")

opcion = int(input("Ingresa tu opción deseada: "))

# if opcion == 1:
#     print()
# elif opcion == 2:
#     print()
# elif opcion == 3:
#     print()
# else: # caso por default
#     print()

match opcion:
    case 1:
        print("Se seleccionó la opción 1...")
    case 2:
        print("Eligió 2...")
    case 3:
        print("Fue 3...")
    case _:
        print("Caso por default.")