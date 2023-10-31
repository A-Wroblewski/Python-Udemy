frase = 'Python é uma linguagem de programação multiparadigma e foi criada por Guido van Rossum.'

letra_mais_repetida = ''
quantidade_letra_mais_repetida = 0

for i in range(len(frase)):
    letra_atual = frase[i]

    if letra_atual == ' ':
        continue

    letra = frase.count(letra_atual)

    if quantidade_letra_mais_repetida < letra:
        quantidade_letra_mais_repetida = letra
        letra_mais_repetida = letra_atual

print(letra_mais_repetida, quantidade_letra_mais_repetida)
