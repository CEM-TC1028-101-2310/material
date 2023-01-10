# Ingresar un número
# Si el número es divisible entre 3 -> Fizz
# Si el número es divisible entre 5 -> Buzz
# Si el número es divisible entre 3 y entre 5 -> FizzBuzz
# Si no es divisible entre 3 ni entre 5 -> número

num = int(input("Ingrese su número: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)