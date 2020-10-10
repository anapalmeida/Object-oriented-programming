
'''
4.
Usando seus conhecimentos de dicionário até agora, implemente a função
conta_letras que recebe uma palavra e retorna um dicionário com o número de
ocorrências de cada letra.

Por exemplo, conta_letras('abacaxi') deve retornar o seguinte dicionário:
    {'a':3,'b':1,'c':1,'x':1}

NÃO USE nenhuma função mágica do python. Escreva a lógica usando dicionários.

O seguinte trecho de código pode ser util:

palavra = 'ganancia'
nro_a = 0
for letra in palavra:
    print('estou olhando para', letra)
    if letra == 'a':,
        nro_a = nro_a+1

Ele produz como resultado:
estou olhando para g
estou olhando para a
estou olhando para n
estou olhando para a
estou olhando para n
estou olhando para c
estou olhando para i
estou olhando para a

E no final, a variável nro_a vai estar valendo 3.
'''

def conta_letras(palavra):
    dic = {}
    for letra in palavra:
        if letra in dic:
            dic[letra] += 1
        else: 
            dic[letra] = 1
    return dic


print(conta_letras('Najwa'))

