frase = 'banana'
lista = ['Banana', 'Maçã', 1, 2, 'Abacaxi', 3]

primeiro, *_, penultimo, ultimo = lista

print(primeiro, penultimo, ultimo)

for i in lista:
    print(i, end=' ')

print()

print(*lista)
print(*frase)
