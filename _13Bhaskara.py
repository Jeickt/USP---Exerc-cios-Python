import math
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta = b **2 - 4*a*c

if delta >= 0:
    if delta > 0:
        resultado1 = (-b + math.sqrt(delta))/(2*a)
        resultado2 = (-b - math.sqrt(delta))/(2*a)
        if resultado1 < resultado2:
            print ("as raízes da equação são", resultado1, "e", resultado2)
        else:
            print ("as raízes da equação são", resultado2, "e", resultado1)
    else:
        resultado = (-b)/(2*a*c)
        print ("a raiz desta equação é", resultado)
else:
    print ("esta equação não possui raízes reais")