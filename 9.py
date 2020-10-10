import math

def imc_calc(peso, altura):
    imc = peso / (math.pow(altura, 2))
    if imc < 17:
      print('Você está muito abaixo do peso! Seu IMC é', round(imc, 2))
    elif imc <= 18.49:
       print('Você está abaixo do peso! Seu IMC é', round(imc, 2))
    elif imc <= 24.99:
           print('Você está com o peso normal. Seu IMC é', round(imc, 2))
    else:
       print('Você está acima do peso. Seu IMC é', round(imc, 2))

altura = float(input('Qual é sua altura? '))
peso = float(input('Qual é seu peso? '))
print(imc_calc(peso, altura))