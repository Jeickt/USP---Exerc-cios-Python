i = 1
while i <= 5:
    j = int(input("Digite um número positivo para cálculo do seu fatorial: "))
    if j >= 0:
        fat = 1
        while j > 1:
            fat = fat * j
            j = j - 1
        print (fat, "\n")
        i = i + 1
    else:
        print("Número inválido!")