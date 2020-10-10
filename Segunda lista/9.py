''' Criar um programa que leia os valores A, B, C, e imprima na tela o maior deles.'''

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))

if a > b and b > c:
    print("O valor ", a, " foi o maior valor digitado")
elif b > a and a > c:
    print("O valor ", b, " foi o maior valor digitado")
else:
    print("O valor ", c, "foi o maior valor digitado")
