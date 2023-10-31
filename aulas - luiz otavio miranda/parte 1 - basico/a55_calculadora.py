while True:
    operadores_validos = '+-*/'

    valor_1 = input('Valor 1: ')
    operador = input('Operador: ')
    valor_2 = input('Valor 2: ')

    try:
        valor_1 = float(valor_1)
        valor_2 = float(valor_2)

        if operador not in operadores_validos:
            print('Operador inválido.')

        if operador == '+':
            soma = valor_1 + valor_2
            print(f'{valor_1} {operador} {valor_2} = {soma:.5f}')
        elif operador == '-':
            subtracao = valor_1 - valor_2
            print(f'{valor_1} {operador} {valor_2} = {subtracao:.5f}')
        elif operador == '*':
            multiplicacao = valor_1 * valor_2
            print(f'{valor_1} {operador} {valor_2} = {multiplicacao:.5f}')
        elif operador == '/':
            divisao = valor_1 / valor_2
            print(f'{valor_1} {operador} {valor_2} = {divisao:.5f}')

    except:
        print('Você precisa digitar números.')

    escolha = input('Para repetir, digite "sim": ').lower().startswith('s')

    if escolha:
        continue
    else:
        break
