from random import choice

lista_palavras = ['abacate', 'acerola', 'abelha', 'banana', 'marmita', 'biruleibe']
palavra_secreta = choice(lista_palavras)
letras_acertadas = ''
tentativas = 0

while True:
    letra_usuario = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_usuario) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_usuario in palavra_secreta:
        letras_acertadas += letra_usuario

    palavra_formatada = ''

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formatada += letra
        else:
            palavra_formatada += '*'

    print(palavra_formatada)

    if palavra_formatada == palavra_secreta:
        break

print(
    f'\nParabéns, você conseguiu!'
    f'\nA palavra secreta era "{palavra_secreta}".'
    f'\nO seu número total de tentativas foi de {tentativas}.'
)
