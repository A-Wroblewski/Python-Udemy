import sys

numero1 = input('Digite o primeiro número: ')
operador = input('Escolha o operador (+, -, *, /): ')
numero2 = input('Digite o segundo número: ')

total = 0

try:
    numero1 = float(numero1)
    numero2 = float(numero2)

    if operador == '+':
        soma = numero1 + numero2
        total += soma

        print(f'Total = {total}')

    elif operador == '-':
        subtracao = numero1 - numero2
        total += subtracao

        print(f'Total = {total}')

    elif operador == '*':
        multiplicacao = numero1 * numero2
        total += multiplicacao

        print(f'Total = {total}')

    elif operador == '/':
        divisao = numero1 / numero2
        total += divisao

        print(f'Total = {total}')

    else:
        print('Operador inválido.')

        sys.exit()

    while True:
        novo_operador = input('Escolha a próxima operação (+, -, *, /): ')
        numero_adicional = input('Digite o número: ')

        try:
            numero_adicional = float(numero_adicional)

            if novo_operador == '+':
                total += numero_adicional

                print(f'Total = {total}')

            elif novo_operador == '-':
                total -= numero_adicional

                print(f'Total = {total}')

            elif novo_operador == '*':
                total *= numero_adicional

                print(f'Total = {total}')

            elif novo_operador == '/':
                total /= numero_adicional

                print(f'Total = {total}')
            
            else:
                print('Operador inválido.')
                print(f'Total = {total}')

                sys.exit()
        
        except ValueError:
            print('Você não digitou um número.')
            print(f'Total = {total}')

            sys.exit()

except ValueError:
    print('Você não digitou um número.')
