import importlib

import A104_modularizacao_M

print(A104_modularizacao_M, '\n')

for i in range(5):
    # módulos são importados apenas uma vez (singleton)
    # import a104_modularizacao_M
    print(i)
    importlib.reload(A104_modularizacao_M)  # recarrega o módulo e o executa novamente

print()

print('Terminou.')
