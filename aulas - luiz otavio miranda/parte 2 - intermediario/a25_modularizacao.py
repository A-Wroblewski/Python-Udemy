import importlib

import a25_modularizacao_M

print(a25_modularizacao_M, '\n')

for i in range(5):
    # módulos são importados apenas uma vez (singleton)
    # import a25_modularizacao_M
    print(i)
    importlib.reload(a25_modularizacao_M)  # recarrega o módulo e o executa novamente

print()

print('Terminou.')
