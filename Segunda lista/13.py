''' Faça um programa que solicite ao usuário o ano e imprima "Ano Bissexto" ou "Ano Não-Bissexto". 
Um ano é bissexto se for divisível por 4, mas não por 100. Um ano também é bissexto se for divisível por 400''
'''

ano = int(input("Digite um ano: "))
if ano % 4 == 0 and ano % 400 == 0:
    print("Esse ano é bissexto!")
else:
    print("Esse ano não é bissexto.")
