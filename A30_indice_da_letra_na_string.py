frase = 'O rato roeu a roupa do rei de Roma.'
tamanho_frase = len(frase)
contador = 0

print(f'A frase "{frase}" tem {tamanho_frase} caracteres.')

while contador < tamanho_frase:
    print(contador, frase[contador])
    contador += 1
