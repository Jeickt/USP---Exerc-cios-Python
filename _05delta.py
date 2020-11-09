a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
import math
delta = b**2 - 4*a*c
if delta >= 0:
    if delta > 0:
        print ("Há resultado duplo para a equação.")
    else:
        print ("Há resultado único para a equação.")
else:
    print ("Não há resultado real para a equação.")