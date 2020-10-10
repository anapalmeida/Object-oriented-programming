'''
1.
Implemente a função consulta que recebe uma agenda (um dicionário)
e uma pessoa, e retorna o telefone dessa pessoa.
'''
def consulta(agenda, pessoa):
    return agenda[pessoa]

agenda = {}
agenda['Lou'] = '99876-1928'
agenda['Debbie'] = '98845-7788'
agenda['Tammy'] = '94940-7788'
agenda['Nine'] = '9938-4043'
agenda['Rose'] = '9349-4043'
agenda['Daphne'] = '9938-3499'
agenda['Amita'] = '9938-2233'
agenda['Constance'] = '9239-4043'

print(consulta(agenda, 'Tammy'))