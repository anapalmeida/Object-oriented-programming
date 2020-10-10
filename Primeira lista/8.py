''' Criar um programa que receba dois valores A e B, e efetue a troca dos valores de forma que a variável A
 passe a possuir o valor da variável B e que a variável B passe a possuir o valor da variável A. 
 Por fim, apresentar os valores trocado. '''


num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

aux = num1
num1 = num2
num2 = aux

print(num1, num2)
