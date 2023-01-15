import functools

produtos = [
    {'nome': 'produto 1', 'preço': 5},
    {'nome': 'produto 2', 'preço': 10},
    {'nome': 'produto 3', 'preço': 15},
    {'nome': 'produto 4', 'preço': 20},
    {'nome': 'produto 5', 'preço': 25},
    {'nome': 'produto 6', 'preço': 30},
    {'nome': 'produto 7', 'preço': 35},
]

soma = functools.reduce(lambda acumulador, produto: acumulador + produto['preço'], produtos, 0)

print(soma)
