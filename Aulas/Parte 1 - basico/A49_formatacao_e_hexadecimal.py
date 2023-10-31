nome = 'Álvaro'
preco = 997.459873
variavel = '%s, o preço é de R$%.2f' %(nome, preco)

print(variavel)

fruta = 'morango'
frase = 'Eu gosto de %s' %fruta

print(f'{frase}\n')

print('O hexadecimal de %d é %x/%X' %(500, 500, 500))
print('O hexadecimal de %d é %04x/%08X' %(500, 500, 500))

print(f'O hexadecimal de 500 é {500:08x}')
print(f'O hexadecimal de 500 é {500:08X}')
