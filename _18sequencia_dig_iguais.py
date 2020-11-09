x = int(input("Digite um número: "))
y = 0
z = 0
dig_iguais = False
while x != 0 and dig_iguais == False:
    y = x % 10
    x = x // 10
    z = x % 10
    if y == z:
        dig_iguais = True

if dig_iguais:
    print ("O número contém dois dígitos em sequência iguais.")
else:
    print ("O número não contém dois dígitos em sequência iguais.")