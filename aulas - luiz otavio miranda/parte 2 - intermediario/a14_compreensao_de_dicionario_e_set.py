dicionario = {
    'a': 1,
    'b': '2',
    'c': 3.0,
    'd': '4',
    'e': '5',
    'f': 6,
    'g': 'peixe',
}

for i in dicionario.items():
    print(i)

print()

dicionario = {
    chave: valor * 2 
    if isinstance(valor, (int, float)) else valor 
    for chave, valor in dicionario.items()
    if valor != 'peixe'
    }

# dicionario = {chave: valor * 2 if isinstance(valor, int) else valor for chave, valor in dicionario.items()}

print(dicionario, '\n')

set_1 = {1, 2, 3, 4, 5, 6}

print(set_1, '\n')

set_2 = {
    numero * 10
    if numero >= 5 else numero
    for numero in range(1, 11)
    if numero < 9
}

print(set_2)
