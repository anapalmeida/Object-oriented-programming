'''
2.
Implemente a função adiciona que recebe uma agenda (um dicionário)
uma pessoa e um telefone, e adiciona o telefone dessa pessoa na agenda.

Adicionar um item num dicionário é simples:
dicionario['chave'] = valor
'''
def adiciona(agenda, pessoa, telefone):
    agenda[pessoa] = telefone
    
agenda = {}
agenda['Lou'] = '99876-1928'
agenda['Debbie'] = '98845-7788'
agenda['Tammy'] = '94940-7788'
agenda['Nine'] = '9938-4043'
agenda['Rose'] = '9349-4043'
agenda['Daphne'] = '9938-3499'
agenda['Amita'] = '9938-2233'
agenda['Constance'] = '9239-4043'

print(adiciona(agenda, 'Ana', '93433-3223'))
print(agenda)