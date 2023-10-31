valores = input().split()
valores = [int(valor) for valor in valores]

valor_buscado = int(input())

if valor_buscado in valores:
    print('Encontrado!')
else:
    print('Não encontrado.')
