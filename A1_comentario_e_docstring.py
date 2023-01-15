# isso é um comentário

print("Linha 1")
print("Linha 2")
print("Linha 3")  # essa é a linha 3
# print("Linha 4")
# abaixo está a linha 5
print("Linha 5")

"""
isso é uma docstring
print("Linha 6")
print("Linha 7")
print("Linha 8")
"""

'''
print("Linha 9")
print("Linha 10")
print("Linha 11")
isso é outra docstring
'''

print("Linha 12")
# acabou

def a():
    '''
    docstring da função
    '''

print(a.__doc__)  # docstrings são lidas junto com o código e podem ser chamadas para obter informações
