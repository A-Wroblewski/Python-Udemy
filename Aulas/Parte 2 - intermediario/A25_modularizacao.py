import importlib

import A25_modularizacao_M

print(A25_modularizacao_M, '\n')

for i in range(5):
    # módulos são importados apenas uma vez (singleton)
    # import A25_modularizacao_M
    print(i)
    importlib.reload(A25_modularizacao_M)  # recarrega o módulo e o executa novamente

print()

print('Terminou.')
