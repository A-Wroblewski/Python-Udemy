# https://docs.python.org/3/library/itertools.html#module-itertools

import itertools

for i in itertools.count(1, 2):  # contador infinito similar ao range
    print(i)

    if i >= 10:
        break

print()

lista = [1, 2, 3]
contador_de_uns = 0

for i in itertools.cycle(lista):  # loop infinito cíclico em um iterável
    if i == 1:
        contador_de_uns += 1

    print(i)

    if contador_de_uns >= 3:
        break

print()

for i in itertools.repeat('banana', 5):
    print(i)
