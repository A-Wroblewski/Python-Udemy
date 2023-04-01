lista_1 = [1, 43, 523, 52543, 637, 46545, 21, 321, 345, 321, 3213]
lista_1.sort()

print(lista_1)

lista_1.sort(reverse=True)

print(lista_1)

lista_2 = [1, 43, 523, 52543, 637, 46545, 21, 321, 345, 321, 3213]

x = sorted(lista_2)

print(x, '\n')

nomes_1 = [
    {'Nome': 'Alícia', 'Sobrenome': 'Cavalcanti'},
    {'Nome': 'João', 'Sobrenome': 'Valentino'},
    {'Nome': 'Zeca', 'Sobrenome': 'Urubu'},
    {'Nome': 'Amanda', 'Sobrenome': 'Antonieta'},
]

def exibir_nomes():
    for itens in nomes_1:
        print(itens)

    print()

def ordenar_por_nome(item):
    return item['Nome']

def ordenar_por_sobrenome(item):
    return item['Sobrenome']

nomes_1.sort(key=ordenar_por_nome)

exibir_nomes()

nomes_1.sort(key=ordenar_por_sobrenome)

exibir_nomes()

nomes_2 = [
    {'Nome': 'Alícia', 'Sobrenome': 'Cavalcanti'},
    {'Nome': 'João', 'Sobrenome': 'Valentino'},
    {'Nome': 'Zeca', 'Sobrenome': 'Urubu'},
    {'Nome': 'Amanda', 'Sobrenome': 'Antonieta'},
]

nomes_2.sort(key=lambda item: item['Nome'])

for itens in nomes_2:
    print(itens)

print()

nomes_2.sort(key=lambda item: item['Sobrenome'])

for itens in nomes_2:
    print(itens)
