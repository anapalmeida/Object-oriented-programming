# Ler as seguintes informações de um funcionário: nome, idade, cargo e o seu salário bruto.
# Considere:
# - O salário bruto teve um reajuste de 38 % .
# - O funcionário receberá uma gratificação de 20 % do salário bruto.
# - O Salário total é descontado em 15%

nome = input('Informe o nome: ')
idade = int(input('Informe a a idade: '))
cargo = input('Informeo cargo: ')
salario = float(input('informe o salario: '))

reajuste = salario * 1.38
reajuste = reajuste * 1.2
reajuste = reajuste * 0.85

print('Salario final R$', reajuste)
