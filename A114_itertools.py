import itertools

armas = ['Cajado', 'Espada', 'Faca', 'Porrete']
classes = ['Assassino', 'Guerreiro', 'Lutador', 'Mago']
raridade = ['Comum', 'Raro', 'Épico', 'Lendário']

print(*list(itertools.combinations(classes, 2)), sep='\n')

print()

print(*list(itertools.permutations(classes, 2)), sep='\n')

print()

print(*list(itertools.product(classes, armas, raridade)), sep='\n')

print()

x = ['a', 'a', 'a', 'a', 'b', 'c', 'a']
x = itertools.groupby(sorted(x))

for valor, grupo in x:
    print(valor, list(grupo))

print()

alunos = [
    {'nome': 'Luiz', 'nota': '10'},
    {'nome': 'Letícia', 'nota': '8'},
    {'nome': 'Fabrício', 'nota': '10'},
    {'nome': 'Rosemary', 'nota': '6'},
    {'nome': 'Joana', 'nota': '4'},
    {'nome': 'João', 'nota': '10'},
    {'nome': 'Eduardo', 'nota': '8'},
    {'nome': 'André', 'nota': '4'},
    {'nome': 'Anderson', 'nota': '6'},
]

alunos_agrupados = sorted(alunos, key=lambda a: a['nota'])
grupos = itertools.groupby(alunos_agrupados, lambda a: a['nota'])

for aluno in alunos_agrupados:
    print(aluno)

print()

for valor, grupo in grupos:
    print(valor, list(grupo))
