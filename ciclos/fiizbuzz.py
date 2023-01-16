
inicio = int(input("Indica el inicio de la secuencia: "))
final = int(input("Indica el final de la secuencia: "))

for i in range(inicio, final+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)