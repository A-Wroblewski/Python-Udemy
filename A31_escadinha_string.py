frase = 'O rato roeu a roupa do rei de Roma.'
tamanho_frase = len(frase)
contador = 0
frase_nova = ''

print(f'A frase "{frase}" tem {tamanho_frase} caracteres.')

while contador < tamanho_frase:
    frase_nova += frase[contador]
    print(frase_nova)
    contador += 1
