fruta = {
    'Nome': 'Maçã',
    'Cor': 'Vermelha',
}

caixa_de_macas = {
    'Quantidade': 16,
    'Caixa': 'Madeira',
}

informacoes_das_macas = {**fruta, **caixa_de_macas}

print(fruta)
print(caixa_de_macas)
print(informacoes_das_macas, '\n')

def dicionar(*args, **kwargs):
    print(f'Argumentos não nomeados: {args}')

    for item in kwargs.items():
        print(f'Argumento nomeado: {item}')

dicionar(1, 2, 3, nome='Mamute', idade=30_000)

print()

dicionar(**informacoes_das_macas)
