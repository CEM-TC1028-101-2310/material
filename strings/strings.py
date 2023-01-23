
# comillas dobles
texto = "Hola mundo"

# comillas sencillas
texto = 'Hola mundo'

# string multilínea
texto = """Hola
mundo"""

# concatenación
texto = "Hola " + "mundo"

# duplicación
texto = "Hola" * 3

# string vacío
texto = ""

texto = "hola mundo"

# Accediendo por medio del índice
# izquierda a derecha -> inicia en 0
print(texto[6])

# derecha a izquierda -> inicia en -1
print(texto[-4])

# Los strings son secuencias inmutables de caracteres
# No se pueden modificar una vez creados

# texto[6] = "s"
# No se puede modificar

s1 = "hola"
s2 = "mundo"
s3 = s1 + s2
print(s1)
print(s2)
print(s3)

# Slicing
texto = "hola mundo"

# inicio:fin -> Igual que en range, no toca a fin
print(texto[3:7])

# inicio: -> Va de inicio hasta el final del string
print(texto[3:])

# :fin -> Va desde el comienzo del string hasta antes de fin
print(texto[:7])

print(texto[:])

# inicio:fin:paso -> Va desde inicio de paso en paso hasta antes de fin
print(texto[3:7:2])

print(texto[::-1])

# Secuencias de escape \
texto = "hola\nmundo" # Salto de línea
print(texto)

texto = "hola\tmundo" # Tabulador o sangría
print(texto)

texto = "hola \"mundo\"" # Incluye las comillas dobles dentro del string
print(texto)

texto = "hola \'mundo\'"
print(texto)

texto = "hola 'mundo'"
texto = 'hola "mundo"'

texto = "hola \\n mundo" # Incluye al caracter de diagonal invertida \ en el texto
print(texto)