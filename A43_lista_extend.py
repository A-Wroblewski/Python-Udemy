lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

print(lista_1, lista_2)
print(lista_1 + lista_2)

lista_1.extend(lista_2)
print(lista_1)

lista_1.extend('a')
print(lista_1)

lista_1.extend('100')
print(lista_1)
