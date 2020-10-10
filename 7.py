from collections import Counter

def contador(frase):
    frase = frase.split(' ')
    print(Counter(frase))

frase = "Mariana Alessandra Ana Mariana Ana Ana"
contador(frase)