frase = input().lower()

lista_vogais = 'aeiou'
lista_vogais = list(lista_vogais)
lista_consoantes = 'bcdfghjklmnpqrstvwxyz'
lista_consoantes = list(lista_consoantes)

vogais = ''
consoantes = ''

for i in frase:
    if i in lista_vogais:
        vogais += i

for i in frase:
    if i in lista_consoantes:
        consoantes += i

print(f'Vogais: {vogais}\nConsoantes: {consoantes}')
