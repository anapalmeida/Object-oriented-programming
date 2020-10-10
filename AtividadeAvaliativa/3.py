'''
3.
Assim sendo, implemente a função verifica, que recebe uma agenda
e um nome de pessoa, e verifica se a pessoa está na agenda
(retorna True se a pessoa está e False caso contrário).
'''
def verifica(agenda, pessoa):
    if pessoa in agenda:
        return True
    else:
        return False

agenda = {}
agenda['Lou'] = '99876-1928'
agenda['Debbie'] = '98845-7788'
agenda['Tammy'] = '94940-7788'
agenda['Nine'] = '9938-4043'
agenda['Rose'] = '9349-4043'
agenda['Daphne'] = '9938-3499'
agenda['Amita'] = '9938-2233'
agenda['Constance'] = '9239-4043'

print(verifica(agenda, 'Lou'))
print(verifica(agenda, 'Ana'))




