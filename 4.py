''' Criar um programa que leia um valor em Real e a cotação do dólar, e converta esse valor em dólares. '''

num1 = float(input('Digite um valor: '))
cotacao = float(input('Cotação do dólar atual:'))

num1 = num1 / cotacao

print('Valor em dólares: $', num1)