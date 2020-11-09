def n_primos(x):
    i = 2
    q = 1

    if x < 2:
        return ("Número inválido!")
    elif x == i:
        return q
    else:
        while x != i:
            while x % i != 0 and x != i:
                i = i + 1
            if x == i:
                q = q + 1
                i = 2
                x = x - 1
            else:
                i = 2
                x = x - 1
        return q

x = int(input("Digite um número igual ou maior que 2: "))
print(n_primos(x))