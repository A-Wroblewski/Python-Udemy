lista = []

elementos_lista = int(input('Deseja botar quantos elementos na lista? '))

for i in range(1, elementos_lista + 1):
    elemento = int(input(f'Digite o {i}° elemento: '))
    lista.append(elemento)

print(lista)
