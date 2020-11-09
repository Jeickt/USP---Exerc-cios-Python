x = int(input("Digite um número: "))
y = []
while x != 0:
    y.append(x)
    x = int(input("Digite um número: "))
i = 0
z = []
while i < len(y):
    z.append(y[-1-i])
    print(z[i])
    i = i + 1