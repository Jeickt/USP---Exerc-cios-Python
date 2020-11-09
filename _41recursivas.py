def main():
    lista1 = [2, 5, 9, 6, 3, 0, 1, 7, 4, 8]
    o = encontra_impares(lista1)
    print(o)


def fatorial(n):
    if n < 1:
        return 1
    else:
        return n * fatorial(n - 1)


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def busca_binaria(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista) - 1

    if max < min:
        return False
    else:
        meio = min + (max - min)//2

    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio-1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio + 1, max)
    else:
        return meio


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista)//2
    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)


def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito

    if not lado_direito:
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])


def soma_lista(lista, n=0):
    if len(lista) == 0:
        return False
    elif len(lista) - 1 == n:
        return lista[n]
    else:
        return lista[n] + soma_lista(lista, n+1)


def encontra_impares(lista, n=0, list=[]):
    if len(lista) == 0:
        return list
    elif len(lista) - 1 == n:
        if lista[n] % 2 != 0:
            list.extend([lista[n]])
            return list
        else:
            return list
    else:
        if lista[n] % 2 != 0:
            list.extend([lista[n]])
            return encontra_impares(lista, n+1, list)
        else:
            return encontra_impares(lista, n+1, list)


main()
