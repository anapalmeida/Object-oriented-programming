''' Uma firma contrata um encanador a 20.000,00 por dia. Crie um programa que solicite 
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, 
sabendo - se que são descontados 8 % para imposto de renda. '''

dias = int(input('Quantos dias você trabalhou? '))
res = 20000 * dias
res = res * 0.08
print('Seu salário com desconto é: ', res)
