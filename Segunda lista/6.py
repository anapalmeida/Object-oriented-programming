''' Criar um programa que leia os valores A e B, compare se a soma de A e B é divisível por 2 e imprima a resposta na tela. '''

a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
a = a+b
if a % 2 == 0:
    print("A soma desses números é divisível por 2")
else:
    print("A soma desses números não é divisível por 2")
