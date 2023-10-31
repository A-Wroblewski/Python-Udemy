lista_1 = [True, True, False, True]

if all(lista_1):  # retorna se todos os itens forem verdadeiros
    print('Verdadeiro.')

else:
    print('Falso')

print()

lista_2 = [True, False, False, True]

if any(lista_2):  # retorna se qualquer item for verdadeiro
    print('Verdadeiro.')

else:
    print('Falso')
