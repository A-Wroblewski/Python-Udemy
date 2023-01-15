numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)

    if numero % 2 == 0:
        print('Seu número é par!')
    else:
        print('Seu número é ímpar!')
except:
    print('Você não digitou um número inteiro.')

###########################################################

hora = input('Digite a hora (de 0 até 23): ')

try:
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print(f'São {hora} horas. Bom dia!')
    elif hora <= 17:
        print(f'São {hora} horas. Boa tarde!')
    elif hora <= 23:
        print(f'São {hora} horas. Boa noite!')
    else:
        print('Você precisa digitar um número de 0 a 23.')
except:
    print('Isso não é um número.')

###########################################################

nome = input('Digite o seu primeiro nome: ')
tamanho_nome = len(nome)

if nome != '':
    if tamanho_nome <= 1:
        print('Digite mais de uma letra.')
    else:
        if tamanho_nome <= 4:
            print('Seu nome é curto!')
        elif tamanho_nome <= 6:
            print('Seu nome é normal!')
        else:
            print('Seu nome é grande!')
else:
    print('Você não digitou nada.')
