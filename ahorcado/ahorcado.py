import random

def elegir_palabra():
    with open("palabras.txt", "r", encoding="utf8") as archivo:
        lista = archivo.readlines()
        palabra = random.choice(lista).strip().lower()
        return palabra
    
def mostrar_ahorcado(errores):
    # Tomado de https://unipython.com/juego-python-ahorcado/
    ahorcado = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    print(ahorcado[len(errores)])
    
def mostrar_palabra(palabra, aciertos):
    res = ""
    for letra in palabra:
        if letra not in aciertos:
            res += "_ "
        else:
            res += letra + " "
    return res

def juego():
    seguir_jugando = "1"
    ganadas = 0
    perdidas = 0
    while seguir_jugando == "1":
        palabra = elegir_palabra()
        aciertos = []
        errores = []
        actual = "_"
        while len(errores) < 6 and "_" in actual:
            
            letra = input("Indica la letra a adivinar: ").strip().lower()
            while not letra.isalpha() or len(letra) != 1 or letra in aciertos + errores:
                print("Debe elegir una letra válida.")
                letra = input("Indica la letra a adivinar: ").strip().lower()
            
            if letra in palabra:
                aciertos.append(letra)
            else:
                errores.append(letra)
                
            mostrar_ahorcado(errores)
            actual = mostrar_palabra(palabra, aciertos)
            print(f"Palabra actual: {actual}")
            print(f"Aciertos: {', '.join(aciertos)}")
            print(f"Errores: {', '.join(errores)}")
        
        print(f"La palabra era: {palabra}")
        if "_" not in actual:
            print("Felicidades, has ganado.")
            ganadas += 1
        else:
            print("Suerte para la próxima, sigue participando.")
            perdidas += 1
            
        while (seguir_jugando := input("¿Desea seguir jugando? 1)Sí, 2)No: ").strip()) not in ["1","2"]:
            print("Debe elegir 1 para sí o 2 para no.")
    print(f"Ganaste {ganadas} veces.")
    print(f"Perdiste {perdidas} veces.")
    
if __name__ == "__main__":
    juego()