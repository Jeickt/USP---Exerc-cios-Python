def fatorial (x):
    fat = 1
    y = x
    
    if (x == 0 or x == 1):
        return fat
    else:
        while (x > 1):
            fat = fat * x
            x = x - 1
        return fat

x = int(input("Digite o maior número: "))
y = int(input("Digite o menor número: "))
coefbi = 1

if x >= y and y >=0:
    coefbi = fatorial(x) / (fatorial(y) * fatorial(x - y))
    print(coefbi)
else:
    print("Números incorretos!")