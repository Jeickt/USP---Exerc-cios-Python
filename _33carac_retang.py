altura = int(input("Digite a altura do retângulo: "))
comprimento = int(input("Digite o comprimento do retângulo: "))
x = 0
y = 0
while y < comprimento:
    if y == 0 or y == (comprimento - 1):
        while x < altura:
            print ("#", end = "")
            x = x + 1
        print ("")
        x = 0
        y = y + 1
    while 0 < y < (comprimento - 1):
        if x == 0 or x == (altura - 1):
            print ("#", end = "")
            x = x + 1
        elif 0 < x < (altura - 1):
            print (" ", end = "")
            x = x + 1
        else:
            print ("")
            x = 0
            y = y + 1
