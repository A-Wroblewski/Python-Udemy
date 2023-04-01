lista = list(range(1, 10))

print(lista)

lista.pop()
print(lista)

lista.append('banana')
print(lista)

lista.insert(5, 50)
print(lista)

del(lista[7:])
print(lista)

print(min(lista))
print(max(lista))

lista.clear()
print(lista)

lista.extend('oi')
print(lista)
