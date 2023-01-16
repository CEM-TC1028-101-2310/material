
n = int(input("Ingrese el valor de n: "))

sumatoria = 0
# 0,1,2,...,n
for k in range(n+1):
    # sumatoria = sumatoria + 2*k + 1
    sumatoria += 2*k + 1
print(f"El resultado de la sumatoria es: {sumatoria}")