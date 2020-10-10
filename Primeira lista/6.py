''' Criar um programa que receba o ano de nascimento de uma pessoa e imprima a sua idade atual. '''
import datetime

idade = int(input('Que ano você nasceu?'))
now = datetime.datetime.now()
idade = now.year - idade
print('Você tem', idade, 'anos')
