import turtle as t
import random

def cuadrado(lado: int):
    for i in range(4):
        t.forward(lado)
        t.left(90)

def figura_regular(lado: int, num_lados: int):
    for i in range(num_lados):
        t.forward(lado)
        t.left(360/num_lados)
    
if __name__ == "__main__":
    t.speed(0)
    for i in range(20):
        n = random.randint(1,100)
        m = random.randint(3,10)
        figura_regular(n,m)
        t.left(5)
#     aux = True
#     for i in range(20):
#         if aux:
#             cuadrado(100)
#         else:
#             pentagono(100)
#         aux = not aux
#         t.left(5)
    t.mainloop()