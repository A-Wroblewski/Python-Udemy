lista = []

for x in range(3):
    for y in range(3):
        lista.append(x)
        lista.append(y)

print(lista)

lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))

print(lista)

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

# lista = [(x, y) for x in range(3) for y in range(3)]

print(lista)
