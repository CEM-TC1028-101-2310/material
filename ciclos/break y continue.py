
for i in range(1,100):
    for j in range(2,200):
        print(f"i: {i}, j: {j}")
        if j % 15 == 0:
            break
    break
print("Fuera del ciclo")   

for i in range(10):
    print(i)
    continue
    print(i,i,i)
    for j in range(200):
        print(j)