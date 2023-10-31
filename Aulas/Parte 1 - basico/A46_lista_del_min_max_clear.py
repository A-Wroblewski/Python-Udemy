lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

del(lista[2:7])
print(lista)

lista.insert(0, 100)
print(lista)

del(lista[0])
print(lista)

print(min(lista))
print(max(lista))

lista.clear()
print(lista)
