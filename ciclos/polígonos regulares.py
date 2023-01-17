import turtle as t

num_lados = int(input("Ingrese el número de lados de su figura: "))
largo_lado = int(input("Ingrese el largo del lado de su figura: "))

angulo = 360 / num_lados

for i in range(num_lados):
    t.forward(largo_lado)
    t.left(angulo)
    
t.mainloop()