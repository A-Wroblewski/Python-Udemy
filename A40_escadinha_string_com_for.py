frase = 'O rato roeu a roupa do rei de Roma.'
tamanho_frase = len(frase)
frase_nova = ''

print(f'A frase "{frase}" tem {tamanho_frase} caracteres.')

for letra in frase:
    frase_nova += letra
    print(frase_nova)
