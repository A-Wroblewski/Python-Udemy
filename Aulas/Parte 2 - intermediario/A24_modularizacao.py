import sys

import A24_modularizacao_M

print('Esse módulo chama-se:', __name__, '\n')

print(*sys.path, sep='\n')

print()

print(A24_modularizacao_M.soma(3, 4, 5, 6, 7))
