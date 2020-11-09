import math
x1 = float(input("Digite o valor de x da primeira coordenada: "))
y1 = float(input("Digite o valor de y da primeira coordenada: "))
x2 = float(input("Digite o valor de x da segunda coordenada: "))
y2 = float(input("Digite o valor de y da segunda coordenada: "))

distancia = math.sqrt((x1 - y1) **2 + (x2 - y2) **2)

if distancia >= 10:
    print ("longe")
else:
    print ("perto")