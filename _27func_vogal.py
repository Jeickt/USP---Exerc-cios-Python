def vogal(x):
    letra = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    b = 0
    
    while b < 10:
        if x == letra[b]:
            return True
            break
        else:
            b = b + 1
    return False
