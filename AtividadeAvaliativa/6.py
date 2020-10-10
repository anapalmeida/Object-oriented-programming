'''
6.
Implemente a função telefone_principal, que recebe uma agenda (nessa versão
mais nova) e uma pessoa. Ela retorna o primeiro telefone da lista de
telefones da pessoa.
'''

def telefone_principal(agenda, pessoa):
    return agenda[pessoa]['telefones'][0]

agenda = {
    'Lou': {
        'email': 'lou.miller@gmail.com.br',
        'telefones': [11999888999, 1177788899]
    },
    'Debbie' : {
        'email': 'debbie.ocean@gmail.com',
        'telefones': [84999777444]
    },
    'Tammy': {
        'telefones': [1177788899]
    }
}

print(telefone_principal(agenda, 'Lou'))
