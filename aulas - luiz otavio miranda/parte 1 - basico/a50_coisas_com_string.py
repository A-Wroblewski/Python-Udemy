nome = input('Digite o seu nome: ')
nome = ' '.join(nome.split())
idade = input('Digite a sua idade: ')

print()

if nome != '' and idade != '':
    espacos = 0

    for letra in nome:
        if letra == ' ':
            espacos += 1

    print(
        f'Seu nome é {nome}!\n\n'
        f'Seu nome invertido é {nome[::-1]}\n'
    )
    
    if ' ' in nome.strip():
        if espacos <= 1:
            print(f'Seu nome contém {espacos} espaço!\n')
        else:
            print(f'Seu nome contém {espacos} espaços!\n')
    else:
        print('Seu nome não tem espaços.\n')

    if len(nome) <= 1:
        print(f'Seu nome tem {len(nome) - espacos} letra.\n')
    else:
        print(f'Seu nome tem {len(nome) - espacos} letras.\n')

    print(
        f'A primeira letra do seu nome é {nome[0]}\n\n'
        f'A última letra do seu nome é {nome[-1]}'
    )
else:
    print('Você deixou algum campo vazio.')
