import copy

pessoa = {
    'Nome': 'Álvaro',
    'Sobrenome': 'Wroblewski',
    'Idade': 19,
    'Idade': 20,
    'Idade': 21,
}

print(pessoa, '\n')

print(len(pessoa), '\n')

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items(), '\n')

pessoa.setdefault('Idade')
pessoa.setdefault('Altura')
print(pessoa['Idade'])
print(pessoa['Altura'])

print(pessoa, '\n')

dicionario_1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'lista': [0, 1, 2]
}

dicionario_2 = copy.deepcopy(dicionario_1)
dicionario_2['d'] = 4
dicionario_2['lista'][0] = 5

print(dicionario_1)
print(dicionario_2, '\n')

chave_removida = dicionario_1.pop('b')

print(chave_removida)
print(dicionario_1)
print(dicionario_2, '\n')

ultima_chave_removida = dicionario_2.popitem()

print(ultima_chave_removida)
print(dicionario_1)
print(dicionario_2, '\n')

print(pessoa)

pessoa.update({
    'Idade': 99999,
    'Cidade': 'Campinas'
})

print(pessoa)
