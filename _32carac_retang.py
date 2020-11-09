altura = int(input("Digite a altura do retângulo: "))
comprimento = int(input("Digite o comprimento do retângulo: "))
x = 0
y = 0
while y < comprimento:
    while x < altura:
        print ("#", end = "")
        x = x + 1
    print ("")
    x = 0
    y = y + 1