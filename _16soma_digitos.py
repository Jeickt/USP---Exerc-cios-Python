x = int(input("Digite um número: "))
soma = 0

while x != 0:
    soma = soma + x % 10
    x = x // 10
print ("A soma dos dígitos do número é igual a", soma)