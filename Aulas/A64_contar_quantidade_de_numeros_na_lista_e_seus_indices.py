valores = input().split()
valores = [int(valor) for valor in valores]

valor_buscado = int(input())

if valor_buscado in valores:
    print(valores.count(valor_buscado))

    for i in range(len(valores)):
        if valores[i] == valor_buscado:
            print(i, end=' ')
else:
    print('Mia x')
