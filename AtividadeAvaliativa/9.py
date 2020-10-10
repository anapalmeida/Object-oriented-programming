'''
9.
Por último, vamos criar uma função conta_ocorrencias
que dirá quantas vezes um telefone ocorre na agenda.

Ela recebe uma agenda melhorada (um dicionário nesse formato
que estamos usando) e devolve um dicionário. As chaves são
os números de telefone, e os valores, às vezes que cada
número apareceu na agenda.
'''


def conta_ocorrencias(agenda):
    dic = {}
    for pessoa in agenda:
        for telefone in agenda[pessoa]['telefones']:
            if telefone in dic:
                dic[telefone] += 1
            else:
                dic[telefone] = 1
    return dic


agenda = {
    'Lou': {
        'email': 'lou.miller@gmail.com.br',
        'telefones': [11999888999, 1177788899]
    },
    'Debbie': {
        'email': 'debbie.ocean@gmail.com',
        'telefones': [84999777444]
    },
    'Tammy': {
        'telefones': [1177788899]
    }
}


print(conta_ocorrencias(agenda))
