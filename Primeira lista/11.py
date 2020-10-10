''' A importância de 780.000,00 será dividida entre os três primeiros colocados de um concurso, 
em partes diretamente proporcionais aos pontos conseguidos por eles. 
Construa um programa que solicite o número de pontos dos três primeiros colocados e imprima a 
importância que caberá a cada um. '''

nome1 = input('Qual é o nome do primeiro colocado? ')
pontos1 = float(input('Quandots pontos fez?'))
nome2 = input('Qual é o nome do segundo colocado? ')
pontos2 = float(input('Quandots pontos fez?'))
nome3 = input('Qual é o nome do terceiro colocado? ')
pontos3 = float(input('Quandots pontos fez?'))

coloc1 = (780000 * pontos1) / 100
coloc2 = (780000 * pontos2) / 100
coloc3 = (780000 * pontos3) / 100

print('O prêmio de', nome1, 'é R$', coloc1, 'que recebeu 50%')
print('O prêmio de', nome2, 'é R$', coloc2, 'que recebeu 25%')
print('O prêmio de', nome3, 'é R$', coloc3, 'que recebeu 25 %')
print('Esses valores foram dividos de', coloc1+coloc2+coloc3)
