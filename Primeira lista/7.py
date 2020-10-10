''' Criar um programa que receba idade de uma pessoa e imprima o seu ano de nascimento. '''
import datetime

idade = int(input('Qual sua idade? '))
now = datetime.datetime.now()
idade = now.year - idade
print('Você nasceu em ', idade)
