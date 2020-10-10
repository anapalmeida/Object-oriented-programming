''' ) Criar um programa que receba o nome de uma pessoa e imprima na tela "Bom dia" com o nome da pessoa.
 Exemplo, o programa que recebe como entrada a palavra "Jadir", terá como saída na tela a frase "Bom dia Jadir". '''

import datetime
now = datetime.datetime.now()
nome = input('Qual é o seu nome? ')
print('Boa noite, ', nome, '.', 'Agora são: ', now.hour, ': ', now.minute)
