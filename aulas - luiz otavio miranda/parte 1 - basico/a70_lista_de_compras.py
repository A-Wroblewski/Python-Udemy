import os

lista_de_compras = []

while True:
    escolha = input(f'\nPara inserir um item na lista, digite 1:'
                        f'\nPara apagar um item da lista, digite 2:'
                        f'\nPara ver como a lista está, digite 3:'
                        f'\nPara finalizar, digite 4: ')

    try:
        escolha = int(escolha)

        if escolha == 1:
            os.system('cls')

            novo_item = input('Digite o nome do item para adicioná-lo: ')
            
            if len(novo_item) == 0 or novo_item.isspace():
                print('Você não digitou nada.')
            else:
                lista_de_compras.append(novo_item)

        elif escolha == 2:
            os.system('cls')

            for indice, item in enumerate(lista_de_compras):
                print(indice, item)

            indice_do_item_a_remover = input('\nDigite o número do item que deseja remover: ')
            
            try:
                indice_do_item_a_remover = int(indice_do_item_a_remover)
                lista_de_compras.pop(indice_do_item_a_remover)

                print(f'\nItem de número {indice_do_item_a_remover} removido.')
            except IndexError:
                print('\nNão há nenhuma item com este número.')
            except ValueError:
                print('Você não digitou um número inteiro.')

        elif escolha == 3:
            os.system('cls')

            if len(lista_de_compras) == 0:
                print('A lista está vazia.')
            else:
                for indice, item in enumerate(lista_de_compras):
                    print(indice, item)

        elif escolha == 4:
            print()
            break

        else:
            os.system('cls')

            print('Opção inválida.')
    except ValueError:
        os.system('cls')

        print('Você não digitou um número inteiro.')

if len(lista_de_compras) == 0:
    print('A sua lista não tem nenhum item.')
else:
    print('Aqui está sua lista:\n')

    for indice, item in enumerate(lista_de_compras):
        print(indice, item)
