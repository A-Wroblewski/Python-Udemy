# Exercício: dizer se o nome do usuário é pequeno, médio ou grande

nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é pequeno.')
elif tamanho_nome > 4 and tamanho_nome <= 6:
    print('Seu nome é médio.')
else:
    print('Seu nome é grande.')
