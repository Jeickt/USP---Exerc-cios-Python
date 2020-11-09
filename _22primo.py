x = int(input("Digite um número inteiro:"))
i = 2

if (i < 100000):
    while (x > i):
        if (x % i != 0):
            i = i + 1
        else:
            print ("não primo")
            break
    if (x == i):
        print ("primo")