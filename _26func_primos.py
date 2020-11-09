def ehprimo(y):
    i = 2

    while y > i:
        if (y % i == 0):
            return True
        else:
            i = i + 1
    return False

def maior_primo(x):
    while ehprimo(x):
        x = x - 1
    return x