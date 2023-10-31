frase = 'O rato roeu a roupa do rei de Roma.'
tamanho_frase = len(frase)
contador = 0
frase_nova = ''

print(f'A frase "{frase}" tem {tamanho_frase} caracteres.')

letra_usuario = input('Deseja trocar os "r" por qual letra? ')

while contador < tamanho_frase:
    letra = frase[contador]

    if letra == 'r':
        frase_nova += letra_usuario
    else:
        frase_nova += letra

    contador += 1

print(frase_nova)
