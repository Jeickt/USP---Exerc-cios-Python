def soma_elementos(x):
    i = 0
    soma = 0
    while i < len(x):
        soma = soma + x[i]
        i = i + 1
    return soma

lista = [1, 2, 2, 4, 3, 7, 5, 5, 9, 1, 0]
print(soma_elementos(lista))
