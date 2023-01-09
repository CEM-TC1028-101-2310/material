# input -> guarda todo valor como texto (str)

udf1 = float(input("Ingresa la calificación de tu udf1: "))
udf2 = float(input("Ingresa la calificación de tu udf2: "))
udf3 = float(input("Ingresa la calificación de tu udf3: "))
udf4 = float(input("Ingresa la calificación de tu udf4: "))
udf5 = float(input("Ingresa la calificación de tu udf5: "))
udf6 = float(input("Ingresa la calificación de tu udf6: "))

promedio = (udf1 + udf2 + udf3 + udf4 + udf5 + udf6) / 6

# Concatenación
print("El promedio de tu semestre fue de: " + str(promedio) + ". Estudia más.")
# Dejarle todo a print y print lo junta con un espacio
print("El promedio de tu semestre fue de:", promedio, ". Estudia más.")
# Usar la función .format
print("El promedio de tu semestre fue de: {0}. Estudia más.".format(promedio))
# f-strings
print(f"El promedio de tu semestre fue de: {promedio}. Estudia más.")

salario = 1563728.7398
print("Tu salario es de: ${0:,.2f}".format(salario))
print(f"Tu salario es de: ${salario:,.2f}")