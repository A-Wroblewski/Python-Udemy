# mapeamento na esquerda e filtro na direita

lista = []

for numero in range(1, 11):
    lista.append(numero)

print(lista, '\n')

lista = [numero * 2 for numero in range(1, 11)]

print(lista, '\n')

produtos = [
    {'nome': 'produto_1', 'preço': 5},
    {'nome': 'produto_2', 'preço': 10},
    {'nome': 'produto_3', 'preço': 15},
    {'nome': 'produto_4', 'preço': 20},
    {'nome': 'produto_5', 'preço': 25},
    {'nome': 'produto_6', 'preço': 30},
]

novos_precos = [
    {**produto, 'preço': produto['preço'] * 2}

    if produto['preço'] > 15 else {**produto}

    for produto in produtos
    ]
# mesma coisa que o comentário abaixo só que separado para ler melhor
# novos_precos = [{**produto, 'preço': produto['preço'] * 2} if produto['preço'] > 15 else {**produto} for produto in produtos]

print(*produtos, sep='\n')
print()
print(*novos_precos, sep='\n')
print()

outros_produtos = [{**produto} for produto in produtos if produto['preço'] >= 20]

print(*outros_produtos, sep='\n')
