
def quita_vocales(texto: str) -> str:
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    for i in vocales:
        texto = texto.replace(i, "")
    return texto
#     res = ""
#     for i in texto:
#         if i not in vocales:
#             # res = res + i
#             res += i
#     return res

def palindromo(texto: str) -> bool:
    texto = texto.replace(" ", "").lower()
    # return texto[::-1] == texto
    for i in range(len(texto)):
        j = len(texto) -1 - i
        if texto[i] != texto[j]:
            return False
    return True

def cambio(texto: str) -> str:
    res = ""
    vocales = "aeiou"
    for i in texto:
#         if i == "a":
#             res += "e"
#         elif i == "e":
#             res += "i"
        if i in vocales:
            if i != "u":
                indice = vocales.find(i) + 1
            else:
                indice = 0
            res += vocales[indice]
        else:
            res += i
    return res

def codificar(texto: str, recorrido: int) -> str:
    texto = texto.lower()
    res = ""
    for i in texto:
        if i.isalpha():
            indice = ord(i) - recorrido
            if indice < ord("a"):
                indice += 26 # letras del abecedario
            res += chr(indice)
        else:
            res += i
    return res
        
if __name__ == "__main__":
    texto = "Hola mundo, ¿cómo estás?"
    resultado = quita_vocales(texto)
    print(resultado)
    
    texto = "No lemon no melon"
    resultado = palindromo(texto)
    print(resultado)
    
    texto = "hola mundo"
    resultado = cambio(texto)
    print(resultado)
    
    texto = "xyz hola mundo abc"
    recorrido = 3
    resultado = codificar(texto, recorrido)
    print(resultado)