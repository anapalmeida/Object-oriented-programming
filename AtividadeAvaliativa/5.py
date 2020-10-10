'''
5.
Implemente a função e-mail, que recebe uma agenda e uma pessoa. Ela retorna 
o e-mail da pessoa.

Não precisa se preocupar com o caso do registro da pessoa não 
ter e-mail (faremos isso mais pra frente).
'''


def email(agenda, pessoa):
    # try:
    return agenda[pessoa]['email']
    # except:
    #   return print('Essa pessoa não tem e-mail!')


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

print(email(agenda, 'Lou'))
print(email(agenda, 'Debbie'))
print(agenda[Debbie])
# print(email(agenda, 'Tammy'))
