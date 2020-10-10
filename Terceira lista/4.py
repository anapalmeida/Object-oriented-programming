''' Dado a lista
L = [91, 10, 50, 89, 45, 80, 2, 45, 3, 105, 95, 13, 26, 49, 50],
criar um programa a que leia um número e verifique e
imprima na tela se este número existe na lista. '''


l = [91, 10, 50, 89, 45, 80, 2, 45, 3, 105, 95, 13, 26, 49, 50]
num = float(input('Digite um número: '))
if num not in l:
    print('Esse número não existe na lista')
else:
    res = l.index(num)
    print('Esse número existe na lista e está na posição', res)
