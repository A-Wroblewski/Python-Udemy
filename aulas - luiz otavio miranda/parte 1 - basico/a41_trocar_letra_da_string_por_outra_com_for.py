frase = 'O rato roeu a roupa do rei de Roma.'

print(frase)

letra_removida = input('Deseja substituir qual letra da frase? ')
letra_adicionada = input(f'Digite a letra que substituirá o {letra_removida}: ')

frase_nova = ''

for letra in range(len(frase)):
    letra_atual = frase[letra]

    if letra_atual == letra_removida:
        frase_nova += letra_adicionada
    else:
        frase_nova += letra_atual

print(frase_nova)
