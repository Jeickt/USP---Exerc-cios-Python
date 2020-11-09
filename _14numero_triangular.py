x = int(input("Digite um número que talvez seja triangular: "))

i = 1
j = 0

while i < 100:
    if x == i * (i+1) * (i+2):
        print ("O número é resultado da multiplicação de:", i, i+1, i+2)
        j = 1
        i = i + 100
    else:
        i = i + 1

if j != 1:
    print ("O número não é resultado da multiplicação de 3 números consecutivos.")