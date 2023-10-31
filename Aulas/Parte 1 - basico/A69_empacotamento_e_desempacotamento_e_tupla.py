_, _, letra, *_ = ['A', 'B', 'C', 'D', 'E', 'F']

# _ -> variável lixo

print(letra, _)
print()

tupla = 'a', 'b', 'c'
outra_tupla = ('a', 'b', 'c')
lista = ['a', 'b', 'c']

print(tupla, outra_tupla, lista)

tupla = list(tupla)
lista = tuple(lista)

print(tupla, lista)
print()

for i, j in enumerate(lista):
    print(i, j)

print()

for item in enumerate(tupla):
    i, j = item
    print(i + 1, j)

print()

t1 = ['1', '2', 3]
t2 = enumerate(t1)

print(t1, t2)

t2 = list(enumerate(t1))

print(t2)
print()

listinha = [1, 2, [], 3, 4, [8, 9, 10, [], [[15, []], 12, 13, 14], 11], 5, [], 6, 7]
print(listinha[5][4][0][0])
