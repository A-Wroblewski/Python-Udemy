# não difere no tanto de memória usada importar o módulo todo ou apenas uma parte

import sys  # importa o módulo inteiro e protege o nome do objeto
from math import sqrt  # importa o objeto desejado sem proteção de nome
import random as hihihihohoho  # renomeia o módulo
from os import name as ertgfeiuywg  # renomeia o objeto

platform = 'batata'
sqrt = 'pamonha'

print(platform)
print(sys.platform)
print(platform, '\n')

# ocorre um erro pois o objeto foi sobrescrito por outra variável do mesmo nome
# print(sqrt(64))
print(sqrt, '\n')

print(hihihihohoho.randint(1, 10), '\n')

print(ertgfeiuywg)

sys.exit()

print(2)
