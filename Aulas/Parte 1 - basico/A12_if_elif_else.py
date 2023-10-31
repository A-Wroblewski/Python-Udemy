num_1 = 5
num_2 = 5

expressao_1 = num_1 == num_2
expressao_2 = num_1 != num_2
expressao_3 = num_1 > num_2
expressao_4 = num_1 >= num_2
expressao_5 = num_1 < num_2
expressao_6 = num_1 <= num_2

print(
    f'{expressao_1}\n'
    f'{expressao_2}\n'
    f'{expressao_3}\n'
    f'{expressao_4}\n'
    f'{expressao_5}\n'
    f'{expressao_6}'
)

print()  # Exercício: alguém só consegue empréstimo se tiver mais de 17 anos de idade

idade = int(input('Qual sua idade? '))

if idade >= 18:
    print('Você pode pedir empréstimo!')
else:
    print('Você não pode pedir empréstimo.')

print()  # Exercício: alguém só consegue empréstimo se tiver mais de 19 e menos de 31 anos de idade

idade = int(input('Qual sua idade? '))

if idade >= 20 and idade <= 30:
    print('Você pode pedir empréstimo!')
else:
    print('Você não pode pedir empréstimo.')
