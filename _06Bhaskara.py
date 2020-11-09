import math
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta = b **2 - 4*a*c

if delta >= 0:
    if delta > 0:
        resultado1 = (-b + math.sqrt(delta))/(2*a)
        resultado2 = (-b - math.sqrt(delta))/(2*a)
        print ("Há resultado duplo para a equação:", resultado1, resultado2)
    else:
        resultado = (-b)/(2*a*c)
        print ("Há resultado único para a equação:", resultado)
else:
    print ("Não há resultado real para a equação.")