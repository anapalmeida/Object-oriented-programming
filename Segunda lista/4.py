''' Criar um programa que receba uma temperatura em Fahrenheit e a tranforme para graus centígrados. A conversão de graus Fahrenheit (F) para graus centígrados (C) é obtida através da fórmula C = 5/9(F-32).'''


tempF = float(input("Qual é a temperatura em Fahrenheit? "))
tempC = (tempF - 32) * 5/9
print("A tempetatura em centígrados é", tempC)
