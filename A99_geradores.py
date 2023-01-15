import sys

lista = [n for n in range(10_000)]  # valores salvos na memória no momento em que a lista é criada
gerador = (n for n in range(10_000))  # valores não são salvos na criação do gerador

print(lista, '\n')
print('Tamanho da lista em bytes =', sys.getsizeof(lista), '\n')

print(gerador, '\n')

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador), '\n')

print('Tamanho do gerador em bytes =', sys.getsizeof(gerador))
