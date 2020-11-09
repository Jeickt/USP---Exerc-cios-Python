def main ():
    apresentacao()
    if escolha_inicial() == 1:
        op(1)
        print("****Começa a partida****")
        partida()
        print("****Final da partida!****\n\nPlacar: Você 0 X 1 Computador\n\n")
        print("Lembre-se da regra 3. Espero que tenha se divertido!\n")
    else:
        op(2)
        print("****Começa o campeonato!****")
        i = 1
        while i < 5:
            if i < 4:
                print("**** Rodada", i, "****")
                i = i + 1
                partida()
            else:
                i = 5
                print("****Final do campeonato!****\n\nPlacar: Você 0 X 3 Computador\n\n")
                print("Lembre-se da regra 3. Espero que tenha se divertido!\n")
       

def apresentacao ():
    print("""Bem vindo ao jogo do NIM!\n\nNeste jogo, um número de peças é disposto em um tabuleiro. Numa partida, você pode escolher o número total de peças e a quantidade máxima que pode ser retirada do tabuleiro por cada jogador em cada rodada. Quem retirar a última peça do tabuleiro vence o jogo.\n\nRegras:\na) A quantidade mínima de peças no tabuleiro deve ser igual ou maior a 2.\nb) A quantidade máxima de peças que pode ser retirada deve necessariamente ser menor que a quantidade total de peças do tabuleiro;\nc) Divirta-se!\n\n""")

def escolha_inicial():
    print("Escolha:\n")
    i = 1
    while i == 1:
        print("Você prefere jogar uma partida ou um campeonato?")
        opc = int(input("Para uma partida digite '1'. Para um campeonato digite '2': "))
        if opc == 1 or opc ==2:
            i = 2
            return opc
        else:
            print("Opção inválida")
 

def op(x):
    if x == 1:
        print("\n\nVocê escolheu uma partida.\n\n")
    if x == 2:
        print("\n\nVocê escolheu um campeonato!\n\n")
 

def partida():
    n = 0
    m = 0
    i = 1
    while n < 2:
        n = int(input("Qual o número total de peças que haverá no tabuleiro? "))
        if n < 2:
            print("Ops! Número inválido! Leia a regra 'a)'.")
    while m < 1 or m >= n:
        m = int(input("Qual a quantidade de peças que pode ser retirada por jogada? "))
        if m < 1 or m >= n:
            print("Ops! Número inválido Leia a regra 'c)'.") 

    if n % (m + 1) == 0:
        print("\nVocê começa.\n")
        while n > 0:
            if i == 1:
                n = n - usuario_escolhe_jogada(n, m)
                i = 2
            else:
                n = n - computador_escolhe_jogada(n, m)
                i = 1
        print("O computador ganhou!\n\n")
        i = 1
    else:
        print("\nO computador começa.\n")
        while n > 0:
            if i == 1:
                n = n - computador_escolhe_jogada(n, m)
                i = 2
            else:
                n = n - usuario_escolhe_jogada(n, m)
                i = 1
        print("O computador ganhou!\n\n")
        i = 1
        

def computador_escolhe_jogada(n, m):
    i = n
    j = m
    while n == i:
        if n == m:
            n = n - m
            if m == 1:
                print("O computador tirou", m, "peça.\n")
            else:
                print("O computador tirou", m, "peças.\n")
            return m
        if (n - m) % (j + 1) == 0:
            n = n - m
            if n - m == 0:
                if m == 1:
                    print("O computador tirou", m, "peça.\n")
                else:
                    print("O computador tirou", m, "peças.\n")
                return m
            else: 
                if m == 1:
                    print("O computador tirou", m, "peça.")
                    if n == 1:
                        print("Agora resta apenas", n, "peça no tabuleiro.\n")
                    else:
                        print("Agora restam apenas", n, "peças no tabuleiro.\n")
                else:
                    print("O computador tirou", m, "peças.")
                    if n == 1:
                        print("Agora resta apenas", n, "peça no tabuleiro.\n")
                    else:
                        print("Agora restam apenas", n, "peças no tabuleiro.\n")
                return m
        elif (m > 1):
            m = m - 1
        else:
            n = n - j
            if j == 1:
                print("O computador tirou", j, "peça.")
                if n == 1:
                    print("Agora resta apenas", n, "peça no tabuleiro.\n")
                else:
                    print("Agora restam apenas", n, "peças no tabuleiro.\n")
            else:
                print("O computador tirou", j, "peças.")
                if n == 1:
                    print("Agora resta apenas", n, "peça no tabuleiro.\n")
                else:
                    print("Agora restam apenas", n, "peças no tabuleiro.\n")
            return j


def usuario_escolhe_jogada(n, m):
    x = n
    y = m
    while n == x:
        m = int(input("Quantas peças você vai tirar? "))
        if 0 < m <= y:
            n = n - m
            if m == 1:
                print("\nVocê tirou", m, "peça.")
                if n == 1:
                    print("Agora resta apenas", n, "peça no tabuleiro.\n")
                else:
                    print("Agora restam apenas", n, "peças no tabuleiro.\n")
            else:
                print("\nVocê tirou", m, "peças.")
                if n == 1:
                    print("Agora resta apenas", n, "peça no tabuleiro.\n")
                else:
                    print("Agora restam apenas", n, "peças no tabuleiro.\n")
        else:
            print("Ops! Jogada Inválida! Tente novamente.")
    return m

main()