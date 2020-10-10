''' Refaça o exercício 11, identificando o conceito aprovado(média superior a 6), exame(média entre 4 e 6) ou reprovado(média inferior a 4)'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media > 6:
    print("Você foi aprovado e sua média é ", media)
elif media >= 4 and media <= 6:
    print("Você pode fazer o exame e sua média é", media)
elif media < 6:
    print("Você foi reprovado e sua média é ", media)
