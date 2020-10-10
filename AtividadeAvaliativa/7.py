'''
7.
Se você quiser verificar todas as chaves de um dicionário,
pode fazer como a seguir:

for chave in agenda_melhor:
    print(chave)

Ele vai produzir como saída:
Jadir
Maria
Caio

Assim sendo, implemente a função sem_email, que recebe uma
agenda (nessa versão mais nova) e retorna uma lista de todos
os contatos sem e-mail.

Por exemplo, sem_email(agenda_melhor1) deve retornar uma
lista com um único contato: ['Caio']
'''


def sem_email(agenda):
    dic = []
    for pessoa in agenda:
        if 'email' in agenda[pessoa].keys():
            pass
        else:
            dic.append(pessoa)
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
    },
    'Nine': {
        'telefonessss': [1177788899]
    }
}

print(sem_email(agenda))
