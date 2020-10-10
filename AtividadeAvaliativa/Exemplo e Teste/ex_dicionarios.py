# AC 1 - Alunos Caio Santos / Jadir Mendonça

agenda_1 = {}
agenda_1['marcos'] = '99876-1928'
agenda_1['alessandra'] = '98845-7788'
agenda_1['maria'] = '94940-7788'
agenda_1['caio'] = '9938-4043'

'''
1.
'''


def consulta(agenda, pessoa):
    return agenda[pessoa]


'''
2.
'''


def adiciona(agenda, pessoa, telefone):
    agenda[pessoa] = telefone


'''
3.

'''


def verifica(agenda, pessoa):
    if pessoa in agenda:
        return True
    else:
        return False


'''
4.
'''


def conta_letras(palavra):
    dic = {}
    for letra in palavra:
        if letra in dic:
            dic[letra] += 1
        else:
            dic[letra] = 1
    return dic


agenda_melhor1 = {
    'Lucas': {
        'email': 'lucas.goncalves@faculdadeimpacta.com.br',
        'telefones': [11999888999, 1177788899]
    },
    'Maria': {
        'email': 'maria.aparecida@exemplo.com',
        'telefones': [84999777444]
    },
    'Caio': {
        'telefones': [1177788899]
    }
}

'''
5.
'''


def email(agenda, pessoa):
    return agenda[pessoa]['email']


'''
6.
'''


def telefone_principal(agenda, pessoa):
    return agenda[pessoa]['telefones'][0]


'''
7.
'''


def sem_email(agenda):
    dic = []
    for pessoa in agenda:
        if 'email' in agenda[pessoa].keys():
            pass
        else:
            dic.append(pessoa)
    return dic


'''
8.
'''


def conta_telefones(agenda):
    return sum(len(agenda[pessoa]['telefones']) for pessoa in agenda)


'''
9.
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
