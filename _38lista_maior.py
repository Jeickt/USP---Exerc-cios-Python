def maior_elemento(x):
    i = 1
    y = x[0]
    while i < len(x):
        if x[i] > y:
            y = x[i]
            i = i + 1
        else:
            i = i + 1
    return y

lista = [1, 2, 2, 4, 3, 7, 5, 5, 9, 1, 0]
print(maior_elemento(lista))
