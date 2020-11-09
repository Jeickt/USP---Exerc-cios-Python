def soma_hipotenusas(y):
    soma = 0
    while y > 1:
        if é_hipotenusa(y) != 0:
            soma = soma + é_hipotenusa(y)
            y = y - 1
        else:
            y = y - 1
    return soma

def é_hipotenusa(z):
    i = 1
    j = 1
    while z > i:
        while z > j:
            if (z ** 2) == (i ** 2) + (j ** 2):
                i = 1
                j = 1
                return z
            else:
                j = j + 1
        j = 1
        i = i + 1
    i = 1
    j = 1
    return 0

x = int(input("Digite um número igual ou maior que 2: "))
print(soma_hipotenusas(x))