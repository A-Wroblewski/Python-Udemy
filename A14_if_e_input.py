usuario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

usuario_bd = 'Álvaro'
senha_bd = 'banana123'

print()

if usuario == usuario_bd and senha == senha_bd:
    print('Você está logado!')
elif usuario != usuario_bd and senha == senha_bd:
    print('Usuário incorreto.')
elif usuario == usuario_bd and senha != senha_bd:
    print('Senha incorreta.')
else:
    print('Usuário e senha incorretos.')
