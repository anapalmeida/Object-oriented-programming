''' Criar um programa que leia os valores A, B, N, compare se a soma de A e B é divisível por N e imprima a resposta na tela.  '''

a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
c = float(input("Digite mais um número: "))
a = a+b
if a % c == 0:
    print("A soma desses números é divisível por ", c)
else:
    print("A soma desses números não é divisível por ", c)
