import copy
import operator

produtos = [
    {'nome': 'Produto 5', 'preço': 10.00},
    {'nome': 'Produto 1', 'preço': 22.32},
    {'nome': 'Produto 3', 'preço': 10.11},
    {'nome': 'Produto 2', 'preço': 105.87},
    {'nome': 'Produto 6', 'preço': 93.99},
    {'nome': 'Produto 4', 'preço': 69.90},
]

print('Tabela original dos produtos: ', '\n')
print(*produtos, sep='\n')
print()

novos_produtos = copy.deepcopy(produtos)

# aumenta preço dos produtos em 10%
novos_produtos = [{**produto, 'preço': round(produto['preço'] * 1.1, 2)} for produto in produtos]

print('Tabela original dos produtos com preço aumentado em 10%: ', '\n')
print(*novos_produtos, sep='\n')
print()

produtos_ordenados_por_nome = copy.deepcopy(produtos)

# ordena os produtos por nome decrescente
produtos_ordenados_por_nome = sorted(produtos, key=operator.itemgetter('nome'), reverse=True)

print('Tabela original dos produtos ordenados pelo nome de maneira decrescente: ', '\n')
print(*produtos_ordenados_por_nome, sep='\n')
print()

produtos_ordenados_por_preco = copy.deepcopy(produtos)

# ordena os produtos por preço crescente
produtos_ordenados_por_preco = sorted(produtos, key=operator.itemgetter('preço'))

print('Tabela original dos produtos ordenados pelo preço de maneira crescente: ', '\n')
print(*produtos_ordenados_por_preco, sep='\n')
