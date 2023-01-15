pessoa = {
    'Nome': 'Álvaro',
    'Sobrenome': 'Wroblewski',
    'Idade': 21,
    'Altura': 1.75,
    'Endereços': [
        {
            'Lugar 1': 'eni ayuoki',
            'Número': 123
        },
        {
            'Lugar 2': 'Rua dos Bobos',
            'Número': 0
        }
    ]
}

print(pessoa, type(pessoa))

print()

print(pessoa['Sobrenome'])
print(pessoa['Endereços'])

print()

for i, j in pessoa.items():
    print(i, j)

print()

for i in pessoa.items():
    print(i)

print()

pessoa['Cidade'] = 'Campinas'
print(pessoa)

print()

for i in pessoa.items():
    print(i)

print()

nova_chave = 'Estado'
teste = 'fruta'

pessoa[nova_chave] = 'São Paulo'
pessoa[teste] = 'abacaxi'

print(pessoa)
print()

del pessoa['fruta']

print(pessoa)

print()

print(pessoa.get('Estado'))
print(pessoa.get('fruta'))

if pessoa.get('yugdsc'):
    print('Existe.')
else:
    print('Não existe.')

print()

if pessoa.get('Cidade') is None:
    print('Não existe.')
else:
    print('Existe.')
