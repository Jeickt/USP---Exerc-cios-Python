x = int(input("Digite um número: "))
y = x
fatorial = 1

if (x < 0):
    print ("O número não é natural!")
elif (x == 0 or x == 1):
    print (fatorial)
else:
    while (x > 1):
        fatorial = fatorial * x
        x = x - 1
    print (fatorial)