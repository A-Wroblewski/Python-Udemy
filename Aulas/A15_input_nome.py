usuario = input('Digite seu usuário: ')
quantidade_caracteres = len(usuario)

print()

print(f'{usuario}, {quantidade_caracteres}, {type(quantidade_caracteres)}')

if quantidade_caracteres >= 6:
    print('Nome aprovado!')
else:
    print('Insira no mínimo 6 caracteres.')
