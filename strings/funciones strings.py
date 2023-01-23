
texto = "Hola mundo"
texto = texto.upper() # Generando un nuevo string con el string original en mayúsculas
print(texto)

texto = "Hola mundo"
primera = texto[:len(texto)//2].upper()
segunda = texto[len(texto)//2:]
texto = primera + segunda
print(texto)