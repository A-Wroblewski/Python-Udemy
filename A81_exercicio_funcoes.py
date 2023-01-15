def criar_multiplicacao(multiplicador):
    def multiplica(numero):
        return numero * multiplicador

    return multiplica

numero_usuario = float(input('Escolha um número: '))

duplicar_numero = criar_multiplicacao(2)
triplicar_numero = criar_multiplicacao(3)
quadruplicar_numero = criar_multiplicacao(4)
quintuplicar_numero = criar_multiplicacao(5)
sextuplicar_numero = criar_multiplicacao(6)
setuplicar_numero = criar_multiplicacao(7)
octuplicar_numero = criar_multiplicacao(8)
nonuplicar_numero = criar_multiplicacao(9)

print()

print(f'Número duplicado = {duplicar_numero(numero_usuario):.2f}')
print(f'Número triplicado = {triplicar_numero(numero_usuario):.2f}')
print(f'Número quadruplicado = {quadruplicar_numero(numero_usuario):.2f}')
print(f'Número quintuplicado = {quintuplicar_numero(numero_usuario):.2f}')
print(f'Número sextuplicado = {sextuplicar_numero(numero_usuario):.2f}')
print(f'Número setuplicado = {setuplicar_numero(numero_usuario):.2f}')
print(f'Número octuplicado = {octuplicar_numero(numero_usuario):.2f}')
print(f'Número nonuplicado = {nonuplicar_numero(numero_usuario):.2f}')
