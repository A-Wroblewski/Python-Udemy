while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Selecione a operação (+, -, *, /): ')

    try:
        num_1 = float(num_1)
        num_2 = float(num_2)

        if operador == '+':
            soma = num_1 + num_2
            print(f'{soma:.2f}')
        elif operador == '-':
            subtracao = num_1 - num_2
            print(f'{subtracao:.2f}')
        elif operador == '*':
            multiplicacao = num_1 * num_2
            print(f'{multiplicacao:.2f}')
        elif operador == '/':
            divisao = num_1 / num_2
            print(f'{divisao:.2f}')
        else:
            print('Operador inválido.')

            finalizar = input('Se quiser finalizar o programa, digite "sair".')
    
            if finalizar == 'sair':
                break
            
            continue
    except:
        print('Você não digitou um número.')

    finalizar = input('Se quiser finalizar o programa, digite "sair".')

    if finalizar == 'sair':
        break
