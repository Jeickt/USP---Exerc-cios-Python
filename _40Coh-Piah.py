import re

def main ():
    modelo = le_assinatura()
    textos = le_textos()
    ass_textos = []
    ass_cp = []
    for i in range(len(textos)):
        ass_textos.append(calcula_assinatura(textos[i]))
    for i in range(len(textos)):
        ass_cp.append(compara_assinatura(modelo, ass_textos[i]))
    print ("O texto infectado é o número: ", avalia_textos(textos, ass_cp))


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    cont1 = 0
    while cont1 < 6:
        soma += abs(as_a[cont1] - as_b[cont1])
        cont1 += 1
    grau_similaridade = soma / 6
    return grau_similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    cont_sentencas = len(sentencas)
    frases = []
    palavras = []
    soma_caracteres_sentencas = 0
    cont1 = 0
    while cont1 < cont_sentencas:
        soma_caracteres_sentencas += len(sentencas[cont1])
        frases = frases + separa_frases(sentencas[cont1])
        cont_frases = len(frases)
        soma_caracteres_frases = 0
        cont1 += 1
        cont2 = 0
    while cont2 < cont_frases:
        soma_caracteres_frases += len(frases[cont2])
        palavras = palavras + separa_palavras(frases[cont2])
        cont_palavras = len(palavras)
        soma_caracteres_palavras = 0
        cont2 += 1
        cont3 = 0
    while cont3 < cont_palavras:
        soma_caracteres_palavras += len(palavras[cont3])
        cont3 += 1    
        
    sal = soma_caracteres_sentencas / cont_sentencas
    pal = soma_caracteres_frases / cont_frases
    wal = soma_caracteres_palavras / cont_palavras
    sac = cont_frases / cont_sentencas
    hlr = n_palavras_unicas(palavras) / cont_palavras
    ttr = n_palavras_diferentes(palavras) / cont_palavras
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    infectado = 1000000
    for i in range(len(ass_cp)):
        if ass_cp[i] < infectado:
            infectado = ass_cp[i]
            menor = i + 1
    return menor

main()