frase = 'Meu nome é Álvaro!'

for letra in frase:
    print(letra)

print()

for numerador, letra in enumerate(frase):
    print(numerador, letra)

print()

for letra in enumerate(frase):
    print(letra)
