import re

cpf_digitado_pelo_usuario = input('Digite o CPF que será validado: ')
cpf_digitado_pelo_usuario = re.sub(r'[^0-9]', '', cpf_digitado_pelo_usuario)

try:
    numeros_repetidos = cpf_digitado_pelo_usuario[0] * len(cpf_digitado_pelo_usuario)

    if numeros_repetidos == cpf_digitado_pelo_usuario:
        print('Não repita os números.')

    else:
        # Cálculo primeiro dígito verificador
        cpf_9_primeiros_digitos = cpf_digitado_pelo_usuario[:9]
        soma_cpf_9_primeiros_digitos = 0

        for i in range(len(cpf_9_primeiros_digitos)):
            numero = int(cpf_9_primeiros_digitos[i])

            numero *= (10 - i)
            soma_cpf_9_primeiros_digitos += numero

        primeiro_digito_verificador = (soma_cpf_9_primeiros_digitos * 10) % 11
        primeiro_digito_verificador = 0 if primeiro_digito_verificador > 9 else primeiro_digito_verificador

        # Cálculo segundo dígito verificador
        cpf_9_primeiros_digitos_com_primeiro_verificador = cpf_9_primeiros_digitos + str(primeiro_digito_verificador)
        soma_cpf_9_primeiros_digitos_com_primeiro_verificador = 0

        for i in range(len(cpf_9_primeiros_digitos_com_primeiro_verificador)):
            numero = int(cpf_9_primeiros_digitos_com_primeiro_verificador[i])

            numero *= (11 - i)
            soma_cpf_9_primeiros_digitos_com_primeiro_verificador += numero

        segundo_digito_verificador = (soma_cpf_9_primeiros_digitos_com_primeiro_verificador * 10) % 11
        segundo_digito_verificador = 0 if segundo_digito_verificador > 9 else segundo_digito_verificador

        # Checar se CPF digitado pelo usuário é válido ou não
        cpf_validado = f'{cpf_9_primeiros_digitos}{primeiro_digito_verificador}{segundo_digito_verificador}'
        cpf_validado = print(f'O CPF {cpf_digitado_pelo_usuario} é válido!') if cpf_validado == cpf_digitado_pelo_usuario else print(f'O CPF {cpf_digitado_pelo_usuario} é inválido.')

except IndexError:
    print('Você não digitou números.')
