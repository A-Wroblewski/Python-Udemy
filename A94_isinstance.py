lista = ['a', 1, 2.5, [0, 1], (0, 1), {0, 1}, {'chave': 'valor'}]

for item in lista:
    if isinstance(item, set):
        print(f'{item} = set')

    if isinstance(item, str):
        print(f'{item} = str')

    if isinstance(item, (int, float)):
        print(f'{item} = int ou float')

    if isinstance(item, (list, dict, tuple)):
        print(f'{item} = list, dict ou tupla')
