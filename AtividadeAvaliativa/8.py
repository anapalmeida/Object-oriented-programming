'''
8.
Implemente uma função conta telefones, que recebe uma agenda
(nessa versão mais nova) e retorna a quantidade de números de
telefone registrados.

Se houver telefones repetidos (o exemplo agenda_melhor tem!),
conte as repetições (então, para agenda_melhor1 a resposta deve
ser 4, por mais que o mesmo número apareça no item Caio
e no item Caio '''


def conta_telefones(agenda):
    return sum(len(agenda[pessoa]['telefones']) for pessoa in agenda)


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

print(conta_telefones(agenda))
