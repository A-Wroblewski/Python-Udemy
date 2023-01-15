frase = input()
frase = ''.join(frase.split()).strip().lower()

letra_procurada = input()

print(frase.count(letra_procurada))
