def remove_repetidos(x):
    i = 0
    while i < len(x):
        if x[i] in x[i+1:]:
            del x[i]
        else:
            i = i + 1
    y = sorted(x)
    return y

lista = [1, 2, 2, 4, 3, 7, 5, 5, 9, 1, 0]
print(remove_repetidos(lista))
