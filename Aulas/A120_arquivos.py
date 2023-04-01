# MODOS DE LEITURA:
#
# r -> somente leitura. O arquivo deve existir.
# w -> somente escrita. Ele cria o arquivo caso não exista. Caso exista, o arquivo inteiro é truncado logo na chamada.
# + -> leitura e escrita.
# x -> cria um arquivo. Caso exista, gera um erro.
# a -> mantém o arquivo e adiciona coisas no final dele.
# b -> modo binário.

import os

path = 'A120_arquivos.txt'

# file = open(path, 'w')
# file.close()

with open(path, 'w') as file:  # "with" já fecha o arquivo automaticamente
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

with open(path, 'r') as file:
    print(file.read())

print()

# abre o arquivo com modo de escrita e de leitura
with open(path, 'w+') as file:
    file.write('Linha um\n')
    file.write('Linha dois\n')
    file.writelines(['linha3', 'linha 4\n', 'linha 5\n'])
    file.seek(0)  # volta o cursor do arquivo manipulado para o começo

    print(file.read())

    file.seek(0)

    print('---READLINE---')
    print(file.readline(), end='')  # caso haja quebra de linha no arquivo lido
    print(file.readline().strip())  # elas também seram lidas pelo readline
    print(file.readline())  # isso pode ser arrumado com os métodos acima
    print('---READLINE---\n')

    file.seek(0)

    print('---READLINES---')
    for line in file.readlines():
        print(line.strip())
    print('---READLINES---\n')

with open(path, 'w', encoding='utf-8') as file:
    file.write('Atenção\n')
    file.write('macarrão\n')
    file.write('aéióuç!@#$%¨&*()-_=+<,>.;:/?°\\|')

print('Apagando o arquivo.')

os.remove(path)  # remove o arquivo desejado
# os.rename(path, 'A120_arquivos_renomeado')  # renomeia o arquivo
