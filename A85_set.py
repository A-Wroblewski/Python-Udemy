set_1 = set()
set_2 = {'999', 1, 1, 4, 1, 2, 3, 'banana', 5.5, (100,)}

print(set_1, type(set_1))
print(set_2, '\n')

lista = [1, 1, 1, 1, 1, 2, 3, 2, 3, 2, 3, 1, 2, 3, 4, 1]
lista_para_set = set(lista)
voltar_a_ser_lista = list(lista_para_set)

print(lista)
print(lista_para_set, voltar_a_ser_lista, '\n')

print(1 in set_2)
print(1 not in set_2)
print((100, 101, 102,) in set_2, '\n')

for i in set_2:
    print(i)

print()

set_3 = set()

set_3.add(6)
set_3.add(7)
set_3.add(8)
set_3.add(8)

print(set_3, '\n')

set_3.update('maçã')

print(set_3, '\n')

set_3.update(('pera', 4, 5, 6, 7))

print(set_3, '\n')

set_3.discard(6)
set_3.discard(7)
set_3.discard(8)
set_3.discard('hfdsje')

print(set_3, '\n')

set_3.clear()

print(set_3)
